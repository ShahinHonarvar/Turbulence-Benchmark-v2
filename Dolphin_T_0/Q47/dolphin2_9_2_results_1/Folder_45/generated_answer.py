def palindromes_of_specific_lengths(s):
    substring = s[70:141]
    result = set()
    for length in range(3, 61):
        for i in range(0, len(substring) - length + 1):
            sub = substring[i:i + length]
            lower_sub = sub.lower()
            if lower_sub == lower_sub[::-1] and lower_sub.isalpha():
                result.add(sub)
    return result