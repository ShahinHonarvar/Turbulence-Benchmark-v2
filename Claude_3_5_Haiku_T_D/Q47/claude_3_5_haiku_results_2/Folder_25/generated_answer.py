def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[26:85]
    substr = substr.lower()
    for length in range(30, 47):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if len(candidate) != length:
                continue
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result