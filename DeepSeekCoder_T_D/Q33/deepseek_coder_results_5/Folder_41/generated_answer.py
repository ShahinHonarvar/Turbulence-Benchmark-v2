def return_vowels(s):
    vowels = []
    for char in s[71:81]:
        if 'A' < char <= 'U' and char in 'AEIOU':
            vowels.append(char)
    return vowels