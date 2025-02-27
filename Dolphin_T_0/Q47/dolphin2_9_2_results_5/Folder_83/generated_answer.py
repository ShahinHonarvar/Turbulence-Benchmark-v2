def palindromes_of_specific_lengths(s):
    result = set()
    s = s[75:96].lower()
    for i in range(75, 96):
        for j in range(i + 2, 96):
            sub = s[i:j + 1]
            if sub == sub[::-1] and 7 <= len(sub) <= 9:
                result.add(sub)
    return result