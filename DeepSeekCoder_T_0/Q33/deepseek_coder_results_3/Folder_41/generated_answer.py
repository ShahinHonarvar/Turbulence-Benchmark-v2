def return_vowels(s):
    vowels = []
    for char in s[71:81]:
        if '>' < char <= 'U':
            vowels.append(char)
    return vowels