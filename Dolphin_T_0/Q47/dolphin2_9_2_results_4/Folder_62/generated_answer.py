def palindromes_of_specific_lengths(string):
    substr = string[25:87]
    palindromes = set()
    for length in range(52, 57):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub == sub[::-1] and all((char.isalpha() for char in sub)):
                palindromes.add(sub.lower())
    return palindromes