def palindromes_of_specific_lengths(s):
    filtered_section = ''.join((c for c in s[27:96] if c.isalpha())).lower()
    result = set()
    for length in range(49, 52):
        for i in range(len(filtered_section) - length + 1):
            candidate = filtered_section[i:i + length]
            if candidate == candidate[::-1]:
                result.add(s[27:96][i:s[27:96].index(candidate[-1], i) + 1])
    return result