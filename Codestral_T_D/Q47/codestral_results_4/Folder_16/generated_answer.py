def palindromes_of_specific_lengths(string):
    string = string[15:87]
    palindromes = set()
    for length in range(51, 61):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes