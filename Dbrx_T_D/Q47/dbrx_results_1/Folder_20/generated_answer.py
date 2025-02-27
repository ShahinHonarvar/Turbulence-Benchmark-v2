def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(20, 75):
        for length in range(36, 43):
            substr = s[i:i + length].lower()
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes