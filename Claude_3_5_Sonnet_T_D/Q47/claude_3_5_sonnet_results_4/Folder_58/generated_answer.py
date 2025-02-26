def palindromes_of_specific_lengths(s):
    substr = s[125:284].lower()
    result = set()
    for i in range(len(substr)):
        for j in range(i + 109, min(i + 127, len(substr) + 1)):
            candidate = substr[i:j]
            if candidate.isalpha() and candidate == candidate[::-1]:
                result.add(candidate)
    return result