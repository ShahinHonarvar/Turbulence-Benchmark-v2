def palindromes_of_specific_lengths(s):
    result = set()
    s = s[3:301]
    for length in range(30, 301):
        for i in range(0, len(s) - length + 1):
            substr = s[i:i + length]
            if all((c.isalpha() for c in substr)):
                substr_lower = substr.lower()
                if substr_lower == substr_lower[::-1]:
                    result.add(substr)
    return result