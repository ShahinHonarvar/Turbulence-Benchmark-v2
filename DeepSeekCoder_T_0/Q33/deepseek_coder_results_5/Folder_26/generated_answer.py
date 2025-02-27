def return_vowels(s):
    vowels = []
    for char in s[10:82]:
        if '$' < char <= '@':
            vowels.append(char)
    return vowels