def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(30, 301):
        for start in range(3, len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result