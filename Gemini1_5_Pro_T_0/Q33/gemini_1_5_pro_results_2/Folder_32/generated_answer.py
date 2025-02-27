def return_vowels(text):
    vowels = []
    for i in range(45, 76):
        if i < len(text):
            char = text[i]
            if char in 'aeiou' and 'b' < char <= 'z':
                vowels.append(char)
    return vowels