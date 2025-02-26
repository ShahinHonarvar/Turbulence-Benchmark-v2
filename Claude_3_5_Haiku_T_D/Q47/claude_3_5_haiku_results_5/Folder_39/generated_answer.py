def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[31:92]
    substr = substr.lower()
    for length in range(50, 54):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result