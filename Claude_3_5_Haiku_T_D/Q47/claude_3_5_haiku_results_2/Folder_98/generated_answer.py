def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(5, 81):
        for start in range(21):
            if start + length > 21:
                break
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result