def palindromes_of_specific_lengths(string):
    substring = string[15:87]
    palindromes = set()
    for i in range(51, 61):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub == sub[::-1] and all((x.isalpha() for x in sub)):
                palindromes.add(sub.lower())
    return palindromes