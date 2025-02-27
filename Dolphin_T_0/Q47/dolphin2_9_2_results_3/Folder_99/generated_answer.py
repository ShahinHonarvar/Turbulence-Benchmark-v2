def palindromes_of_specific_lengths(s):
    result = set()
    s = s[127:289]
    for length in range(119, 142):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            sub = ''.join(filter(str.isalpha, sub)).lower()
            if sub == sub[::-1]:
                result.add(sub)
    return result