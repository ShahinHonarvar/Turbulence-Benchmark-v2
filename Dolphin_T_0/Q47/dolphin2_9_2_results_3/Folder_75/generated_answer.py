def palindromes_of_specific_lengths(s):
    s = s[31:75]
    palindromes = set()
    for length in range(22, 40):
        for index in range(len(s) - length + 1):
            substring = s[index:index + length].lower()
            if all((letter.isalpha() for letter in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes