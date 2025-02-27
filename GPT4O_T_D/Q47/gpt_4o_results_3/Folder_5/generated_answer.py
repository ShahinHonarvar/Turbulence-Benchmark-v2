def palindromes_of_specific_lengths(s):
    result = set()
    s = s[63:71].lower()
    s = ''.join(filter(str.isalpha, s))
    n = len(s)
    for length in range(4, 6):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result