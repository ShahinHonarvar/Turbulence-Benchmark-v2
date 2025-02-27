def palindromes_of_specific_lengths(s):
    start_index = 28
    end_index = 94
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    substr = ''.join((c for c in s[start_index:end_index + 1].lower() if c in valid_chars))
    result = set()
    for length in range(38, 50):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result