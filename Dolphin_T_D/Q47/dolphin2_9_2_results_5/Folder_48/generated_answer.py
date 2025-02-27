def palindromes_of_specific_lengths(s):
    substr = s[155:284]
    palindromes = set()
    for i in range(104, 121):
        for j in range(0, len(substr) - i + 1):
            substring = substr[j:j + i]
            if substring == substring[::-1] and all((char.isalpha() for char in substring)):
                palindromes.add(substring.lower())
    return palindromes