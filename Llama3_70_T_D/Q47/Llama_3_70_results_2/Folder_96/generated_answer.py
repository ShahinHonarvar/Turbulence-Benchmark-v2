def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[100:301]
    result = set()
    for length in range(50, 101):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result