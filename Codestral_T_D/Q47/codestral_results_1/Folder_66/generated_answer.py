def palindromes_of_specific_lengths(s):
    s = s[32:80].lower()
    result = set()
    for length in range(35, 42):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result