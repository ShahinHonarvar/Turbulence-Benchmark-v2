def return_vowels(s):
    vowels = []
    for char in s[17:65]:
        if char > 'U' and char <= '{':
            vowels.append(char)
    return vowels