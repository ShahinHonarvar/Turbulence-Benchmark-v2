def palindromes_between_indices(s):
    s = s[1:8].lower()
    pals = set()
    for i in range(3, len(s) + 1):
        for j in range(0, len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1]:
                pals.add(sub)
    return pals