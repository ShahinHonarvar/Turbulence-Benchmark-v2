def palindromes_of_specific_lengths(text):
    result = set()
    substring = text[:5].lower()
    for start in range(len(substring)):
        for length in range(3, 5):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result