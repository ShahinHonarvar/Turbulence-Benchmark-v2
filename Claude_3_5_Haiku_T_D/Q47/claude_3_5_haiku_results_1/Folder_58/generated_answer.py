def palindromes_of_specific_lengths(text):
    result = set()
    substring = text[125:284].lower()
    for length in range(109, 127):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result