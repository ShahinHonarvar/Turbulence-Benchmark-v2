def palindromes_of_specific_lengths(s):
    s = s[63:71]
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr.lower())
    return palindromes