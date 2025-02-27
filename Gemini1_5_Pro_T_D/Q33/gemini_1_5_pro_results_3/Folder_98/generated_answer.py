def return_vowels(text):
    vowels = []
    for i in range(3, 9):
        if i < len(text):
            char = text[i]
            if char in 'AEIOU' and 'S' < char <= 'U':
                vowels.append(char)
    return vowels