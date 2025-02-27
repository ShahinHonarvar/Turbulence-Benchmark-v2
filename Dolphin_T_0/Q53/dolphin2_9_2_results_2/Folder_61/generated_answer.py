def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 5
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes