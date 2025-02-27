def palindromes_between_indices(s):
    result = set()
    for i in range(4, 10):
        for j in range(i, 10):
            substr = s[i:j + 1].lower()
            if len(substr) >= 4 and substr == substr[::-1]:
                result.add(substr)
    return result