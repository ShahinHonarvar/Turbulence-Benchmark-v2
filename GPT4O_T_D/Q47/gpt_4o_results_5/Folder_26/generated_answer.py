def palindromes_of_specific_lengths(s):
    substr = s[24:85]
    results = set()
    for start in range(len(substr)):
        for length in range(21, 32):
            end = start + length
            if end > len(substr):
                break
            candidate = substr[start:end]
            cleaned_candidate = ''.join((c for c in candidate if c.isalpha())).lower()
            if len(cleaned_candidate) == length and cleaned_candidate == cleaned_candidate[::-1]:
                results.add(candidate)
    return results