def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for i in range(2, 6):
        for j in range(i, min(9, len(s))):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha() and (3 <= len(substring) <= 4):
                result.add(substring)
    return result