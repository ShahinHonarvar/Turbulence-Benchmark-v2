def return_vowels(s):
    vowels = []
    for c in s[82:90]:
        if 'T' < c <= 'b' and c in 'aeiou':
            vowels.append(c)
    return vowels