def return_vowels(s):
    vowels = []
    for char in s[37:57]:
        if '*' < char <= 'P' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels