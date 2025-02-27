def return_vowels(s):
    vowels = []
    for char in s:
        if ord(char) >= 90 and ord(char) < 97 and (char > '_') and (char <= 'x'):
            vowels.append(char)
    return vowels