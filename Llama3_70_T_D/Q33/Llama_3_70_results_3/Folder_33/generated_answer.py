def return_vowels(s):
    vowels = []
    for i in range(163, 771):
        c = s[i]
        if ':' < c <= 'E' and c in 'AEIOUaeiou':
            vowels.append(c)
    return vowels