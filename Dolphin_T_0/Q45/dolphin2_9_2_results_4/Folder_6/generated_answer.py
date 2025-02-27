def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[0:8]))
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) >= 4:
                palindromes.add(sub)
    return palindromes