def return_vowels(text):
    vowels = []
    for char in text[28:76]:
        if 'a' <= char <= 'z':
            if char.lower() in 'aeiou':
                vowels.append(char)
    return vowels