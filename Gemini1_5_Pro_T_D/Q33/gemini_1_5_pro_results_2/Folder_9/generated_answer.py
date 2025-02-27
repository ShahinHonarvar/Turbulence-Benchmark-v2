def return_vowels(text):
    vowels = []
    for i in range(13, min(35, len(text))):
        char = text[i]
        if 'A' <= char <= 'F' and ord(char) > 8:
            vowels.append(char)
    return vowels