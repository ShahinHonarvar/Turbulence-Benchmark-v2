def palindromes_of_specific_lengths(s):
    substr = s[35:89]
    palindromes = set()
    for length in range(24, 34):
        for i in range(0, len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub == sub[::-1] and sub.lower() == sub.upper():
                palindromes.add(sub)
    return palindromes