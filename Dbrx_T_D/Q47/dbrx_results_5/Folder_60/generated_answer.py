def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(23, 83):
        for j in range(32, 35):
            if i + j <= 82:
                sub = s[i:i + j].lower()
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes