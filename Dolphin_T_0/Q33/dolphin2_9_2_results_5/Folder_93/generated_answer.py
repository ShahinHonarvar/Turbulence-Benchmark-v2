def return_vowels(text):
    vowels = []
    for char in text[54:82]:
        if '&' < char <= '@' and char in {'a', 'e', 'i', 'o', 'u'}:
            vowels.append(char)
    return vowels