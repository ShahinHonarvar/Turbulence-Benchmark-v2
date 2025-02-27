def return_vowels(s):
    vowels = []
    for char in s:
        if 64 < ord(char) < 82 and 'P' < char <= 'z' and (char in 'AEIOUaeiou'):
            vowels.append(char)
    return vowels