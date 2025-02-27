def palindromes_of_specific_lengths(s):
    substring = s[44:100]
    pal_set = set()
    for length in range(13, 43):
        for i in range(0, len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                pal_set.add(sub)
    return pal_set