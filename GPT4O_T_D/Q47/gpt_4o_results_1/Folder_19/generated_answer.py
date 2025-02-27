def palindromes_of_specific_lengths(s):
    s = ''.join(filter(str.isalpha, s[10:56])).lower()
    n = len(s)
    result = set()
    for length in range(3, 8):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result