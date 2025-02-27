def return_vowels(s):
    vowels = []
    for char in s[260:322]:
        if 'A' < char <= 'U':
            vowels.append(char)
    return vowels