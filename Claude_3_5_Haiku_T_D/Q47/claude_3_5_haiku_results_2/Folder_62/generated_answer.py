def palindromes_of_specific_lengths(text):
    result = set()
    if len(text) < 88:
        return result
    substring = text[26:88].lower()
    for length in range(52, 57):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result