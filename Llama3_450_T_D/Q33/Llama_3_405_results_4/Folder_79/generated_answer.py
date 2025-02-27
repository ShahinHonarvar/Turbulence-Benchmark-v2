def return_vowels(s):
    vowels = 'AEIOUX'
    result = []
    for c in s[74:96]:
        if c in vowels and c > 'I' and (c <= 'X'):
            result.append(c)
    return result