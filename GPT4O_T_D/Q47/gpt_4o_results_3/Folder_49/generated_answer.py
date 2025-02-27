def palindromes_of_specific_lengths(s):
    palindromes = set()
    standardized_substr = ''.join([char.lower() for char in s[10:101] if char.isalpha()])
    n = len(standardized_substr)
    for start in range(n):
        for end in range(start + 10, min(start + 51, n + 1)):
            substr = standardized_substr[start:end]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes