def return_vowels(s):
    vowels = []
    for char in s[56:90]:
        if 'K' < char <= 'z' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels