def return_vowels(s):
    vowels = []
    for char in s[17:65]:
        if 'U' < char <= '{':
            vowels.append(char)
    return vowels