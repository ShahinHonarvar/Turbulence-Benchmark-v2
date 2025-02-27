def palindromes_of_specific_lengths(str):
    res = set()
    for i in range(44, 100):
        for j in range(i + 13, i + 42):
            sub = str[i:j]
            if sub == sub[::-1] and sub.isalpha():
                res.add(sub.lower())
    return res