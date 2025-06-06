def palindromes_of_specific_lengths(s):
    s = s[10:100]
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr.lower() and substr == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes