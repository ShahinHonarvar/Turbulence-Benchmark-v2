def return_vowels(s):
    vowels = []
    for char in s:
        if ord('a') <= ord(char) <= ord('e') and ord('x') < ord(char) < ord('g'):
            vowels.append(char)
    return vowels