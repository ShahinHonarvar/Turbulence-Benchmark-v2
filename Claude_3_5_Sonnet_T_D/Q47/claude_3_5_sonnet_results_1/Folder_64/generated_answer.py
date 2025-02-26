def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:8].lower()
    for i in range(8):
        for j in range(i + 4, min(i + 6, 9)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result