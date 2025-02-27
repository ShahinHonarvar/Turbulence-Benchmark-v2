def return_vowels(s):
    vowels = []
    for char in s[65:70]:
        if 'a' <= char <= 'e':
            vowels.append(char)
    return vowels