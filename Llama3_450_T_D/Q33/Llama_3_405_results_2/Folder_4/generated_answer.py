def return_vowels(s):
    vowels = []
    for c in s[40:91]:
        if 'A' < c <= 'x' and c in 'AEIOUaeiou':
            vowels.append(c)
    return vowels