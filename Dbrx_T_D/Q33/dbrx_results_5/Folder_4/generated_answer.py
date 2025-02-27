def return_vowels(s):
    vowels = []
    for char in s[40:91]:
        if 'A' < char <= 'x' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels