def palindromes_of_specific_lengths(s):
    result = set()
    s = s[23:78]
    for length in range(13, 41):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if sub == sub[::-1]:
                result.add(sub)
    return result