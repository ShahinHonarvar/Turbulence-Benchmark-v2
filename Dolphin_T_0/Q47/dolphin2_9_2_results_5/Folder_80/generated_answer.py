def palindromes_of_specific_lengths(s):
    substring = s[34:89]
    palindromes = set()
    for length in range(24, 34):
        for i in range(0, len(substring) - length + 1):
            if substring[i:i + length] == substring[i:i + length][::-1]:
                if substring[i:i + length].isalpha():
                    palindromes.add(substring[i:i + length].lower())
    return palindromes