def return_vowels(s):
    vowels = []
    for char in s[54:82]:
        if char in 'aeiouAEIOU' and '=' < char <= '@':
            vowels.append(char)
    return vowels