def return_vowels(s):
    vowels = []
    for char in s[328:455]:
        if 'a' <= char <= 'z' and char in 'aeiou':
            vowels.append(char)
    return vowels