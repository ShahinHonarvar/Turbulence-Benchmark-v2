def palindromes_of_specific_lengths(s):
    s = s[26:85]
    s = ''.join(filter(str.isalpha, s)).lower()
    results = set()
    for length in range(30, 47):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                results.add(substring)
    return results