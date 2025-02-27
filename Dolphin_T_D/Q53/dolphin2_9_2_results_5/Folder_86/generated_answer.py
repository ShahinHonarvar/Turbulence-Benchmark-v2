def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = 133
    for i in range(len(s)):
        for j in range(i + n - 1, len(s)):
            sub = s[i:j + 1]
            if all((c.isalpha() for c in sub)):
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes