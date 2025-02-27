def palindromes_of_specific_lengths(s):
    pals = set()
    for i in range(10):
        for j in range(i + 3, min(i + 6, 10)):
            sub = s[i:j]
            if sub == sub[::-1]:
                pals.add(sub.lower())
    return pals