def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:84]
    length_range = range(13, 67)
    filtered_string = ''.join((c for c in substring if c.isalpha()))
    lower_filtered = filtered_string.lower()
    n = len(lower_filtered)
    for start in range(n):
        for length in length_range:
            end = start + length
            if end <= n:
                candidate = lower_filtered[start:end]
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result