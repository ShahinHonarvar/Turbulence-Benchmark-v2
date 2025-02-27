def palindromes_of_specific_lengths(string):
    substring = string[200:301]
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes