def palindromes_of_specific_lengths(s):
    s = s[24:85]
    result = set()
    for length in range(21, 32):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            substring = substring.lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result