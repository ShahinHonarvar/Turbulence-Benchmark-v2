def palindromes_of_specific_lengths(s):
    s = s.lower()
    substr = s[106:281]
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz'
    filtered_substr = ''.join((c for c in substr if c in allowed_chars))
    result = set()
    for l in range(136, 152):
        for i in range(len(filtered_substr) - l + 1):
            candidate = filtered_substr[i:i + l]
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result