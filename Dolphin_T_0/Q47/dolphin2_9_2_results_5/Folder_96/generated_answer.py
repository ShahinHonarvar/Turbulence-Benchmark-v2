def palindromes_of_specific_lengths(s):
    substring = s[100:301]
    result = set()
    for length in range(50, 101):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and all((c.isalpha() for c in sub)):
                result.add(sub.lower())
    return result