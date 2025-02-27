def palindromes_of_specific_lengths(s):
    s = s[:51].lower()
    result = set()
    for length in range(50, 101):
        for start in range(51 - length):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result