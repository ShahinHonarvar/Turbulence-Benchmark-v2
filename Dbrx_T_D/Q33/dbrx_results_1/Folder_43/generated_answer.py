def return_vowels(s):
    vowels = []
    for i in range(22, 82):
        c = s[i]
        if 'N' < c <= 'o' and c in 'aeiou':
            vowels.append(c)
    return vowels