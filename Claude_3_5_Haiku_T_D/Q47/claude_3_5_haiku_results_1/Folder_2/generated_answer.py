def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[10:60].lower()
    for length in range(18, 37):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if len(candidate) == length and all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result