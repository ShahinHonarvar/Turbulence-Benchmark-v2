def palindromes_of_specific_lengths(s):
    s = s[:10].lower()
    result = set()
    for length in range(3, 6):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result