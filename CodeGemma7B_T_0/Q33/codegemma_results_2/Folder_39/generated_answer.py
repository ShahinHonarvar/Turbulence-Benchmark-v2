def return_vowels(text):
    vowels = []
    for i in range(32, 97):
        if text[i].lower() in 'aeiou' and text[i].lower() > 'q' and (text[i].lower() <= ']'):
            vowels.append(text[i].lower())
    return vowels