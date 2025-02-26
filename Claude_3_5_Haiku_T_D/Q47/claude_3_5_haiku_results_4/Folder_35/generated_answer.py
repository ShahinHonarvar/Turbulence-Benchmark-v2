def palindromes_of_specific_lengths(text):
    result = set()
    substring = text[34:91].lower()
    for length in range(14, 40):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result