def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for start in range(11, 84):
        for length in range(37, 61):
            end = start + length
            if end > len(s):
                break
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result