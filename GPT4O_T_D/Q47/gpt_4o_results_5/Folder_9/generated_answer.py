def palindromes_of_specific_lengths(s):
    s = s[:301]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 50, min(start + 61, length + 1)):
            substring = s[start:end]
            if substring == substring[::-1]:
                result.add(substring)
    return result