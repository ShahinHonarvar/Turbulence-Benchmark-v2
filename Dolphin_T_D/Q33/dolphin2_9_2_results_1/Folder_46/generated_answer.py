def return_vowels(s):
    substring = s[10:83]
    vowels = []
    for c in substring:
        if c in 'aeiou' and c > '%' and (c <= 'e'):
            vowels.append(c)
    return vowels