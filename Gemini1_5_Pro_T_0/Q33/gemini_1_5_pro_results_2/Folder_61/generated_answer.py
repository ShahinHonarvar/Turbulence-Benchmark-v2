def return_vowels(text):
    vowels = []
    for i in range(1, min(4, len(text))):
        if text[i] > 'C' and text[i] <= 'I':
            if text[i] in 'AEIOUaeiou':
                vowels.append(text[i])
    return vowels