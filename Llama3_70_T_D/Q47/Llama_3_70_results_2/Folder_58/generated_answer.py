def palindromes_of_specific_lengths(s):
    result = set()
    s = s[125:284].lower()
    for length in range(109, 127):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result