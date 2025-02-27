def return_vowels(s):
    vowels = []
    for char in s[56:68]:
        if 'M' < char <= 'X' and char in 'AEIOU':
            vowels.append(char)
    return vowels