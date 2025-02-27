def palindromes_between_indices(s):
    result = set()
    for i in range(1, 7):
        for j in range(i, 7):
            substring = s[i:j + 1].lower()
            if len(substring) >= 7 and substring == substring[::-1]:
                result.add(substring)
    return result