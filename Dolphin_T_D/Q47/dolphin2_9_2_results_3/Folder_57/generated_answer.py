def palindromes_of_specific_lengths(s):
    s = s[15:95]
    result = set()
    for length in range(39, 53):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if all((c.isalpha() for c in substr)) and substr.lower() == substr[::-1].lower():
                result.add(substr)
    return result