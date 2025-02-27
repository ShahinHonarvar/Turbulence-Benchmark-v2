def palindromes_of_specific_lengths(s):
    s = s[12:123]
    result = set()
    for length in range(12, 221):
        for index in range(len(s) - length + 1):
            substring = s[index:index + length]
            if substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result