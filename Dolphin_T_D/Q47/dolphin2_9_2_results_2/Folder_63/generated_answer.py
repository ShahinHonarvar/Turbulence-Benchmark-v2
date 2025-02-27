def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(26, 32):
        for i in range(33, 86 - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                palindromes.add(s[i:i + length].lower())
    return palindromes if palindromes else set()