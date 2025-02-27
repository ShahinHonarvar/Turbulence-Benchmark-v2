def return_vowels(s):
    vowels = []
    for c in s[11:61]:
        if 'M' < c <= 'W' and c in 'aeiou':
            vowels.append(c)
    return vowels