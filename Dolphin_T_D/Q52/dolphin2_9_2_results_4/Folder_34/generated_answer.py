def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 32):
        if s[i] == s[i + 32]:
            subs = s[i:i + 33]
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes