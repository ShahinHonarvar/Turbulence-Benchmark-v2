def palindromes_between_indices(s):
    substring = s[3:5]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            temp = substring[i:j]
            if len(temp) >= 3 and temp == temp[::-1]:
                result.add(temp.lower())
    return result