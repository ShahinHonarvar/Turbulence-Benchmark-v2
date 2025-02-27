def palindromes_between_indices(s):
    result = set()
    for i in range(1, 6):
        for j in range(6 - i + 1):
            temp = ''.join(sorted([c.lower() for c in s[j:j + i]]))
            if temp == temp[::-1]:
                result.add(temp)
    return result