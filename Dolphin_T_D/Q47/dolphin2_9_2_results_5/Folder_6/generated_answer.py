def palindromes_of_specific_lengths(s):
    result = set()
    s = s[45:99]
    for i in range(40, 48):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1] and all((char.isalpha() for char in sub)):
                result.add(sub.lower())
    return result