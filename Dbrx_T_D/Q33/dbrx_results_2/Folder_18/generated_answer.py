def return_vowels(s):
    vowels = []
    for char in s[528:606]:
        if 'M' < char <= 'X' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels