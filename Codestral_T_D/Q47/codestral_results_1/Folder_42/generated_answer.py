def palindromes_of_specific_lengths(string):
    string = string[43:96]
    palindromes = set()
    for length in range(18, 48):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes