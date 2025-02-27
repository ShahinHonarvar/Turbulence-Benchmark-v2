def palindromes_of_specific_lengths(s):
    s = s[11:98]
    result = set()
    for length in range(29, 63):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                result.add(sub.lower())
    return result