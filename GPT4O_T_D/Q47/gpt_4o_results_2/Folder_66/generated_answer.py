def palindromes_of_specific_lengths(s):
    substr = s[32:80]
    substr = ''.join(filter(str.isalpha, substr)).lower()
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes