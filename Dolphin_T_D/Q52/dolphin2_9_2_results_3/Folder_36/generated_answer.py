def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 338, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes