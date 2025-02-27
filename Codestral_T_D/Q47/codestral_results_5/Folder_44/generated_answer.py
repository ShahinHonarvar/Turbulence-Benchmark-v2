def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(31, 52):
        for i in range(18, 99 - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes