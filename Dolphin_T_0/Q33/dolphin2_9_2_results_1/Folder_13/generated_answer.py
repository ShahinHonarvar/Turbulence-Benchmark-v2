def return_vowels(s):
    vowels = []
    for i in range(149, 313):
        if 'M' < s[i] <= 'j' and s[i].lower() in 'aeiou':
            vowels.append(s[i])
    return vowels