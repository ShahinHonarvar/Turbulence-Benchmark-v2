def return_vowels(text):
    vowels = []
    for char in text[2:7]:
        if '^' < char <= 'd':
            vowels.append(char)
    return vowels