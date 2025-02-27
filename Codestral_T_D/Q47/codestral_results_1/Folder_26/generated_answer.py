def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(21, 32):
        for i in range(24, 85 - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1]:
                if substring.isalpha():
                    palindromes.add(substring)
    return palindromes