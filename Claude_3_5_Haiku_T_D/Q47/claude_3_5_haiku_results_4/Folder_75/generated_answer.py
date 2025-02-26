def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(23, 40):
        for start in range(31, 75 - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result