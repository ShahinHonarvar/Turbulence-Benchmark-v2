def palindromes_of_specific_lengths(s):
    s = s[23:95]
    result = set()
    for i in range(17, 56):
        for j in range(0, len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result