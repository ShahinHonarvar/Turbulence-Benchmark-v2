def palindromes_of_specific_lengths(string):
    substring = string[65:100]
    palindromes = set()
    for i in range(26, 34):
        for j in range(i, len(substring) + 1):
            sub = substring[j - i:j]
            sub = ''.join(filter(str.isalpha, sub)).lower()
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes