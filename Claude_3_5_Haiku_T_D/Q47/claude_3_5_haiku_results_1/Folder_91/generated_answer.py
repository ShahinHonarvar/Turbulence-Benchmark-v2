def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:11].lower()
    for length in range(3, 6):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if len(substring) == length and substring.isalpha() and (substring == substring[::-1]):
                result.add(substring)
    return result