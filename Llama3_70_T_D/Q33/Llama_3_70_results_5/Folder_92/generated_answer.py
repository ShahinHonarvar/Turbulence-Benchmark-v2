def return_vowels(s):
    vowels = []
    for char in s[3:8]:
        if 'A' < char <= 'D' and char in 'AEIOU':
            vowels.append(char)
    return vowels