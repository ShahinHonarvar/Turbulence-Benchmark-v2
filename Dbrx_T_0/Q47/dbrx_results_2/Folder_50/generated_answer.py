def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(10, 36):
        for i in range(36, len(s) - length + 1):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes