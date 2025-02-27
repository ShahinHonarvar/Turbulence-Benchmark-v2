def return_vowels(s):
    vowels = []
    for char in s[1:4]:
        if 'C' < char <= 'I' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels