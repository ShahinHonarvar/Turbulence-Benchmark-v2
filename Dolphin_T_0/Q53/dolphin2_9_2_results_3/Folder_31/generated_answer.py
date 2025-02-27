def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 34, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes