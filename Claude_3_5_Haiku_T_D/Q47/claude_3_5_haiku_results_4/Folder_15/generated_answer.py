def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(3, 7):
        for start in range(7 - length + 1):
            substr = s[start:start + length].lower()
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes