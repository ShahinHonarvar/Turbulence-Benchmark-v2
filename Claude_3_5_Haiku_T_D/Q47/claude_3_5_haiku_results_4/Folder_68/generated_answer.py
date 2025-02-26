def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(50, 101):
        for start in range(51):
            substring = s[start:start + length]
            if len(substring) == length and substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result