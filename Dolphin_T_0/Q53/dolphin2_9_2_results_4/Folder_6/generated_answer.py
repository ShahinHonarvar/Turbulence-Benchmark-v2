def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) >= 22:
                palindromes.add(sub)
    return palindromes