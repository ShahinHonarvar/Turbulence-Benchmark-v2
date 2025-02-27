def palindromes_of_specific_lengths(s):
    result = set()
    s = s[30:85].lower()
    for length in range(12, 21):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substr)
    return result