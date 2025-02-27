def palindromes_of_specific_lengths(s):
    s = s[:31]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for length in range(20, 31):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if sub == sub[::-1]:
                result.add(sub)
    return result