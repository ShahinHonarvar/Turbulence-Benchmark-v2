def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(20, 22):
        for i in range(12, 56 - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes