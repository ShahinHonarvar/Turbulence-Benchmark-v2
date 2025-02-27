def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(109, 127):
        for i in range(125, 283 - length + 2):
            substring = s[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result