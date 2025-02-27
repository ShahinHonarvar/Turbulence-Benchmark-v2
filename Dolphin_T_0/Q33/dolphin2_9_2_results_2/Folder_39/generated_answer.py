def return_vowels(text):
    vowels = []
    for char in text:
        if ord(char) >= ord('Q') and ord(char) <= ord(']'):
            vowels.append(char)
    return vowels