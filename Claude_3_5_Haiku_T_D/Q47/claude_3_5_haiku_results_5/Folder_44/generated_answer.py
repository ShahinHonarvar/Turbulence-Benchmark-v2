def palindromes_of_specific_lengths(text):
    result = set()
    substring = text[18:99].lower()
    for length in range(31, 52):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if len(candidate) == length and all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result