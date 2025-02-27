def return_vowels(s):
    vowels = []
    for char in s[21:23]:
        if 'a' <= char <= 'n' and char in 'aeiou':
            vowels.append(char)
    return vowels