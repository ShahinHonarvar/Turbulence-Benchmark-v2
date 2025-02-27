def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(24, 53):
        for start_index in range(10, 71 - length):
            if s[start_index:start_index + length] == s[start_index:start_index + length][::-1]:
                result.add(s[start_index:start_index + length])
    return result