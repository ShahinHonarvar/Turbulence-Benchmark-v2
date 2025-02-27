def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(65, 100):
        for length in range(26, 34):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes