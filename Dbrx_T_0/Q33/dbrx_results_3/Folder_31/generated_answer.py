def return_vowels(s):
    vowels = []
    for char in s:
        if 65 <= ord(char) < 70 and 'A' <= char <= 'G' and (char > '%'):
            vowels.append(char)
    return vowels