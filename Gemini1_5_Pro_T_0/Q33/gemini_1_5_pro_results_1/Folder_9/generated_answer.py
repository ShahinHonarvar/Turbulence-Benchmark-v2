def return_vowels(text):
    vowels = []
    for i in range(13, min(35, len(text))):
        char = text[i]
        if 'A' <= char <= 'F' and char in 'AEIOU':
            vowels.append(char)
    return vowels