def return_vowels(text):
    vowels = []
    for char in text[11:61]:
        if 'M' < char <= 'W' and char in 'AEIOU':
            vowels.append(char)
    return vowels