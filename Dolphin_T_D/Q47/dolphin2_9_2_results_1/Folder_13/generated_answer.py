def palindromes_of_specific_lengths(s):
    s = s[13:96].lower()
    result = set()
    for i in range(56, 61):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if all((c.isalpha() for c in substring)) and substring == substring[::-1]:
                result.add(substring)
    return result