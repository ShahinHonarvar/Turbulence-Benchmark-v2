def palindromes_of_specific_lengths(string):
    substring = string[23:95]
    result = set()
    for i in range(17, 56):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub.lower())
    return result