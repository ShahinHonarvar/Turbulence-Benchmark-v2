def return_vowels(text):
    vowels = []
    for i in range(23, 85):
        if i < len(text):
            char = text[i]
            if char in 'aeiouAEIOU' and char > 'W' and (char <= 'v'):
                vowels.append(char)
    return vowels