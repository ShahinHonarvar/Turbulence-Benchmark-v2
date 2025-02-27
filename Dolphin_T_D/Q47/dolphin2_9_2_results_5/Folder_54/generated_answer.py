def palindromes_of_specific_lengths(s):
    substring = s[27:78]
    palindromes = set()
    for length in range(18, 20):
        for i in range(len(substring) - length + 1):
            if all((c.isalpha() for c in substring[i:i + length])):
                if substring[i:i + length].lower() == substring[i:i + length].lower()[::-1]:
                    palindromes.add(substring[i:i + length].lower())
    return palindromes