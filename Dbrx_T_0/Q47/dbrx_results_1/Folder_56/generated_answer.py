def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(3, 8):
        for i in range(1, 10 - length + 1):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes