def palindromes_between_indices(s):
    letters = ''.join(sorted([c for c in s[4:10] if c.isalpha()]))
    n = len(letters)
    palindromes = set()
    if n >= 3:
        for i in range(n):
            for j in range(i + 3, n + 1):
                sub = letters[i:j]
                if len(sub) >= 7 and sub == sub[::-1]:
                    palindromes.add(sub.lower())
    return palindromes