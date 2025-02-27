def palindromes_of_specific_lengths(s):
    result = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(18, 66):
        for j in range(23, 37):
            if i + j - 1 <= 65:
                substring = s[i:i + j].lower()
                if set(substring) <= english_letters and substring == substring[::-1]:
                    result.add(substring)
    return result