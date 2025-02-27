def return_vowels(string):
    vowels = []
    for c in string[32:62]:
        if c in 'aeiouAEIOU' and c > '?' and (c <= 'p'):
            vowels.append(c)
    return vowels