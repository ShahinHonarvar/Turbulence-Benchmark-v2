def palindromes_of_specific_lengths(s):
    result = set()
    s = s[15:78]
    for length in range(43, 48):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring.lower())
    return result