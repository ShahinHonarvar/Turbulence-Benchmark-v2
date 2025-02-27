def return_vowels(s):
    vowels = []
    for char in s[604:949]:
        if 'N' < char <= 'U' and char in 'AEIOU':
            vowels.append(char)
    return vowels