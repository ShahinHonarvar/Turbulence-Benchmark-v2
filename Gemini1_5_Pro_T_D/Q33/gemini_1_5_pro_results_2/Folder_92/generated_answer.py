def return_vowels(text):
    vowels = []
    for i in range(3, 8):
        if i < len(text) and ';' < text[i] <= 'D':
            if text[i] in 'AEIOUaeiou':
                vowels.append(text[i])
    return vowels