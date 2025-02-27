def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            sub = s[i:j]
            if len(sub) >= 30 and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes