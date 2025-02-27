def return_vowels(text):
    vowels = []
    for i in range(13, 37):
        if i < len(text) and 'Z' < text[i] <= '}':
            if text[i] in 'AEIOUaeiou':
                vowels.append(text[i])
    return vowels