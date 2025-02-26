def palindromes_of_specific_lengths(text):
    text = text.lower()
    result = set()
    if len(text) <= 122:
        return result
    substring = text[12:123]
    for length in range(12, 221):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result