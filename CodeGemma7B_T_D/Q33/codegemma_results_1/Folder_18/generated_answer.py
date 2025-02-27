def return_vowels(string):
    s = string[528:606]
    vowels = []
    for c in s:
        if c in 'aeiouAEIOU' and 'M' < c <= 'X':
            vowels.append(c)
    return vowels