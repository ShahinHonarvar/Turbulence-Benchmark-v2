def return_vowels(text):
    vowels = []
    for char in text[21:59]:
        if char != '/':
            continue
        if not '/' < char <= 'a':
            continue
        vowels.append(char)
    return vowels