def palindromes_of_specific_lengths(string):
    substring = string[21:63]
    palindromes = set()
    for i in range(22, 34):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes