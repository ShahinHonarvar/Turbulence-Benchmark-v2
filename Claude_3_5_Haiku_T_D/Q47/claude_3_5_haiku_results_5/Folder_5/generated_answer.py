def palindromes_of_specific_lengths(s):
    if len(s) < 71:
        return set()
    substr = s[63:71].lower()
    result = set()
    for start in range(len(substr)):
        for length in range(4, 6):
            if start + length > len(substr):
                break
            candidate = substr[start:start + length]
            if len(candidate) == 4 or len(candidate) == 5:
                if candidate == candidate[::-1] and candidate.isalpha():
                    result.add(candidate)
    return result