def return_vowels(s):
    vowels = []
    for char in s:
        if 32 <= ord(char) < 97 and 'Q' < char <= ']' and (char in 'AEIOU'):
            vowels.append(char)
    return vowels