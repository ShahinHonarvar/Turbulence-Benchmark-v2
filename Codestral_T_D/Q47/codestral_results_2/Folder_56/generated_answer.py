def palindromes_of_specific_lengths(s):
    s = s[1:10]
    s = s.lower()
    result = set()
    for length in range(3, 8):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result