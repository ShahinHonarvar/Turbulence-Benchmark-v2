def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[12:123]
    for length in range(12, 221):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.lower() == substr.lower()[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes