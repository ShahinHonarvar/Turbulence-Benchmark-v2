def return_vowels(string):
    vowels = []
    for char in string:
        if 65 <= ord(char) < 70 and '%' < char <= 'G':
            vowels.append(char)
    return vowels