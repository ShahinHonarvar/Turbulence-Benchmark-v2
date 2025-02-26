def palindromes_of_specific_lengths(text):
    if len(text) < 301:
        return set()
    substring = text[200:301]
    result = set()
    for length in range(10, 51):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            lowercase_candidate = candidate.lower()
            if lowercase_candidate == lowercase_candidate[::-1] and lowercase_candidate.isalpha():
                result.add(candidate)
    return result