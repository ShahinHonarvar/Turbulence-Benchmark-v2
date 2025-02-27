def return_vowels(text):
    vowels = []
    for i in range(23, 75):
        if i < len(text):
            char = text[i]
            if char in 'aeiouAEIOU' and 'L' < char <= 'd':
                vowels.append(char)
    return vowels