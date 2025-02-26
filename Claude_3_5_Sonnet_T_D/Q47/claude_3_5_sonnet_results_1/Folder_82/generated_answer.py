def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(3, min(301, len(s))):
        for j in range(i, min(301, len(s))):
            substring = s[i:j + 1]
            if substring == substring[::-1] and substring.isalpha() and (30 <= len(substring) <= 300):
                result.add(substring)
    return result