def palindromes_between_indices(s):
    substring = s[2:7]
    result = set()
    for i in range(3, len(substring) + 1):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub == sub[::-1]:
                result.add(sub.lower())
    return result