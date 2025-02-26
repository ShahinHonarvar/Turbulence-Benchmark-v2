def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for length in range(3, 11):
        for start in range(1, 300):
            if start + length > len(s):
                break
            substr = s[start:start + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes