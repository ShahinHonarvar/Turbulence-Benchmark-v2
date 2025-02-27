def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(20, 31):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes