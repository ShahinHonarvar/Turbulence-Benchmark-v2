def palindromes_of_specific_lengths(s):
    result = set()
    s = s[1:8].lower()
    alphas = [c for c in s if c.isalpha()]
    for start in range(len(alphas)):
        for end in range(start + 3, min(start + 5, len(alphas) + 1)):
            sub = ''.join(alphas[start:end])
            if sub == sub[::-1]:
                result.add(sub)
    return result