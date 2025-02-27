def return_vowels(s):
    vowels = []
    for char in s[23:57]:
        if 'a' <= char <= 'd' and char in 'aeiou':
            vowels.append(char)
    return vowels