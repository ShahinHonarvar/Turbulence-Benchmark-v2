def palindromes_of_specific_lengths(s):
    s = s[100:201]
    palindromes = set()
    for length in range(5, 11):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and all((char.isalpha() for char in substring)):
                palindromes.add(substring)
    return palindromes