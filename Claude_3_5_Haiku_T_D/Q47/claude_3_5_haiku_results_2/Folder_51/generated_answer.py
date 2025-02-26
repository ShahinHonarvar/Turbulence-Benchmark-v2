def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for start in range(2, 7):
        for length in range(3, 5):
            if start + length > len(s):
                break
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result