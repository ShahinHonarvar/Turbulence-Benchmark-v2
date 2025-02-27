def palindromes_of_specific_lengths(s):
    substring = s[30:96]
    result = set()
    for i in range(34, 56):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub == sub[::-1] and sub.isalpha() and (sub.lower() == sub):
                result.add(sub)
    return result