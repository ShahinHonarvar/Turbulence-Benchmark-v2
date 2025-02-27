def palindromes_of_specific_lengths(s):
    substr = s[23:83]
    result = set()
    for length in range(32, 35):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            filtered_candidate = ''.join(filter(str.isalpha, candidate))
            if len(filtered_candidate) == length and filtered_candidate.lower() == filtered_candidate[::-1].lower():
                result.add(candidate)
    return result