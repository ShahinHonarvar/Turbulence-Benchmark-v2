def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(23, 39):
        for i in range(41, 90 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result