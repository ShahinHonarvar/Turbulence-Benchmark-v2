def return_vowels(text):
    vowels = []
    for i in range(14, 60):
        if i < len(text):
            char = text[i]
            if char in 'aeiouAEIOU' and char > 'D' and (char <= 'v'):
                vowels.append(char)
    return vowels