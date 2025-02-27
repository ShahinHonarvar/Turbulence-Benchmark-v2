def return_vowels(s):
    vowels = []
    for c in s[10:82]:
        if '$' < c <= '@' and c in 'aeiouAEIOU':
            vowels.append(c)
    return vowels