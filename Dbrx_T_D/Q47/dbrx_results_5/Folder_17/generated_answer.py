def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(22, 96):
        for length in range(52, 56):
            substring = s[i:i + length].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes