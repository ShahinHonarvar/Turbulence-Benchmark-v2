def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 22):
        subs = s[i:i + 23]
        if subs == subs[::-1]:
            palindromes.add(subs)
    return palindromes