def palindromes_of_specific_lengths(s):
    length = len(s)
    s_substring = s[10:60]
    s_palindromes = set()
    for length in range(18, 37):
        for i in range(length, length + 36):
            sub = s_substring[i - length:i]
            if sub == sub[::-1] and sub.lower() == sub.upper():
                s_palindromes.add(sub)
    return s_palindromes