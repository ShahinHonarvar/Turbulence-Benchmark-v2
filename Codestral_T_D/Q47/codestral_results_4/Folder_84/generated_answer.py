def palindromes_of_specific_lengths(string):
    string = string[23:78].lower()
    palindromes = set()
    for length in range(13, 41):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes