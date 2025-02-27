def return_vowels(s):
    vowels = []
    for char in s[3:8]:
        if ';' < char <= 'D' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels