def palindromes_of_specific_lengths(string):
    string = string[13:100]
    palindromes = set()
    for length in range(26, 30):
        for start in range(len(string) - length + 1):
            substring = string[start:start + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes