def return_vowels(s):
    vowels = []
    for char in s[34:69]:
        if 'a' <= char <= 'o' and char > '_':
            vowels.append(char)
    return vowels