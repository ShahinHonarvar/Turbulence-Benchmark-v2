def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[124:284]
    for length in range(115, 135):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                result.add(candidate)
    return result