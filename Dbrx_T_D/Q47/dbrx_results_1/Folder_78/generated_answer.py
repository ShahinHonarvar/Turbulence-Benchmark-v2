def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(19, 56):
        for index in range(15, len(string) - length + 2):
            substring = string[index:index + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes