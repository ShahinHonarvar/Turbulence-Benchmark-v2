def palindromes_of_specific_lengths(s):
    s = s[14:91]
    result = set()
    for length in range(55, 72):
        for start_idx in range(0, 90 - length + 1):
            subset = s[start_idx:start_idx + length]
            subset_lower = subset.lower()
            if subset_lower == subset_lower[::-1] and subset.isalpha():
                result.add(subset)
    return result