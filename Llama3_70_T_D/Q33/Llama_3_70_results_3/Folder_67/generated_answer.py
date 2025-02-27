def return_vowels(s):
    vowels = []
    for char in s[21:59]:
        if '/' < char <= 'a':
            vowels.append(char)
    return vowels