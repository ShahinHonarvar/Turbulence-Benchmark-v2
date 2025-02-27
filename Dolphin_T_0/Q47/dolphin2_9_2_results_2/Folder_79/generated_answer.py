def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(3, 5):
        for i in range(1, 9):
            if i + length > 9:
                break
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes