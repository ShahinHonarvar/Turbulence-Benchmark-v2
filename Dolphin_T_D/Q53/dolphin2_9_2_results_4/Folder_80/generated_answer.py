def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            t = s[i:j]
            if len(t) >= 30 and t == t[::-1]:
                palindromes.add(t)
    return palindromes