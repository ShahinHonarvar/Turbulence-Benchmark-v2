def palindromes_of_specific_lengths(some_string):
    substring = some_string[30:96]
    palindromes = set()
    for i in range(34, 56):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub == sub[::-1]:
                palindromes.add(''.join(filter(str.isalpha, sub)))
    return palindromes