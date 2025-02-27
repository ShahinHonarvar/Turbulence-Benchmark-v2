def return_vowels(s):
    vowels = []
    for char in s[54:82]:
        if '=' < char <= '@' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels