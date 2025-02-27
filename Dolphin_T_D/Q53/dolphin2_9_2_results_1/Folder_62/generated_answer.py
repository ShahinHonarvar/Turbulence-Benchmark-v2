def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 30):
        for j in range(i + 31, len(s) + 1):
            sub = s[i:j]
            if all((c.isalpha() for c in sub)) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes