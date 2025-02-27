def palindromes_of_specific_lengths(s):
    substring = s[15:87]
    palindromes = set()
    for i in range(len(substring) - 50):
        for j in range(i + 51, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1] and all((char.isalpha() for char in sub)):
                palindromes.add(sub.lower())
    return palindromes