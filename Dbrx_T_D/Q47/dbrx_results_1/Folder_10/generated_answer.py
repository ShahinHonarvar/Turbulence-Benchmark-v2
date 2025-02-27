def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(16, 40):
        for i in range(16 - length, 61 - length):
            if s[i:i + length].lower().isalpha():
                substring = s[i:i + length].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes