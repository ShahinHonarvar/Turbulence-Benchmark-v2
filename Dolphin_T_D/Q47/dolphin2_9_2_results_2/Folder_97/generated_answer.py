def palindromes_of_specific_lengths(s):
    substring = s[28:95]
    palindromes = set()
    for i in range(38, 50):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes