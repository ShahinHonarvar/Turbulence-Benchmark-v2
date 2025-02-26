def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for start in range(13, 96):
        for length in range(57, 61):
            if start + length > len(s):
                break
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result