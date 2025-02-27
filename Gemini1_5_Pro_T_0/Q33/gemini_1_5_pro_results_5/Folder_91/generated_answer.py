def return_vowels(text):
    vowels = []
    for i in range(4, 8):
        if i < len(text):
            char = text[i]
            if char in 'aeiouAEIOU' and char > 'P' and (char <= 'r'):
                vowels.append(char)
    return vowels