def return_vowels(s):
    vowels = []
    for c in s[21:23]:
        if 'a' < c <= 'n' and c in 'aeiou':
            vowels.append(c)
    return vowels