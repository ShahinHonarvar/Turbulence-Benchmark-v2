def palindromes_between_indices(s):
    result = set()
    for i in range(2, 4):
        for j in range(i, len(s)):
            substring = s[i:j + 1].lower()
            if len(substring) >= 3 and substring == substring[::-1]:
                result.add(substring)
    return result