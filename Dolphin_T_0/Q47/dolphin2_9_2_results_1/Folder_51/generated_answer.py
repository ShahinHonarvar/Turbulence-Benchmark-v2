def palindromes_of_specific_lengths(s):
    s = s[2:9].lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 2, len(s) + 1):
            sub = s[i:j]
            if all((c.isalpha() for c in sub)) and len(sub) in [3, 4] and (sub == sub[::-1]):
                palindromes.add(sub)
    return palindromes