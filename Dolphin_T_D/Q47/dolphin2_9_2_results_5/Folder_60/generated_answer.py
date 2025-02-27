def palindromes_of_specific_lengths(s):
    substring = s[23:83]
    result = set()
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length].lower()
            if sub == sub[::-1]:
                result.update(set(sub))
    return result