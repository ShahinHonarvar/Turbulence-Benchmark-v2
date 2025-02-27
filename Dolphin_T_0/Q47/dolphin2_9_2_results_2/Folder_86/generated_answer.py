def palindromes_of_specific_lengths(string):
    string = string[30:96]
    palindromes = set()
    for length in range(34, 56):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes