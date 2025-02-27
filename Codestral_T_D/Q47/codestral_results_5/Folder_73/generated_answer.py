def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[21:63]
    for length in range(22, 34):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindromes.add(sub)
    return palindromes