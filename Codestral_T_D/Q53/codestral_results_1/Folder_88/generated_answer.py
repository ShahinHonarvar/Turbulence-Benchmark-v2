def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 27
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha() and (len(sub) >= n):
                palindromes.add(sub)
    return palindromes