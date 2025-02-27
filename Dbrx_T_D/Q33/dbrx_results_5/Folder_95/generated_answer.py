def return_vowels(string):
    vowels = []
    for char in string:
        if 32 <= ord(char) < 61 and 'A' <= char <= 'P' and (char in 'AEIOU'):
            vowels.append(char)
    return vowels