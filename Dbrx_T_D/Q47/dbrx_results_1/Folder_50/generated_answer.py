def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(10, 36):
        for index in range(36, len(s) - length + 2):
            substring = s[index:index + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes