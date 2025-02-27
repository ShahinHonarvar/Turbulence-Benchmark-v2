def palindromes_of_specific_lengths(string):
    string = string[16:95]
    palindromes = set()
    for length in range(39, 53):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if all((c.isalpha() for c in substring)) and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes