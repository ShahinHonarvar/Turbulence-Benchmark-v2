def palindromes_of_specific_lengths(s):
    if len(s) < 85:
        return set()
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    substring = s[30:85]
    results = set()
    length_range = range(12, 21)
    for start in range(len(substring)):
        for length in length_range:
            end = start + length
            if end <= len(substring):
                candidate = substring[start:end]
                filtered_candidate = ''.join((c for c in candidate if c in valid_chars))
                candidate_lower = filtered_candidate.lower()
                if candidate_lower == candidate_lower[::-1] and len(candidate_lower) in length_range:
                    results.add(candidate_lower)
    return results