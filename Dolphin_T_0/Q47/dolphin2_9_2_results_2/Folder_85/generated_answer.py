def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[29:99]
    for i in range(6, 10):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1] and all((char.isalpha() for char in sub)):
                palindromes.add(sub.lower())
    return palindromes