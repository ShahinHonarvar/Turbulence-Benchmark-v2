def palindromes_of_specific_lengths(s):
    s = s[21:63]
    palindromes = set()
    for length in range(22, 34):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and all((letter.isalpha() for letter in substring)):
                palindromes.add(substring)
    return palindromes