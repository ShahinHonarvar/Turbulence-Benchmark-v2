def return_vowels(text):
    vowels = []
    for i in range(11, min(61, len(text))):
        char = text[i]
        if char in 'AEIOUaeiou' and 'M' < char <= 'W':
            vowels.append(char)
    return vowels