def palindromes_of_specific_lengths(s):
    s = s[40:95].lower()
    result = set()
    for length in range(45, 52):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substr)
    return result