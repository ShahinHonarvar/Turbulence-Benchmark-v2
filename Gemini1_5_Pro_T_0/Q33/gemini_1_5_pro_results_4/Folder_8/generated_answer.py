def return_vowels(text):
    vowels = []
    for i in range(64, 82):
        if i < len(text):
            char = text[i]
            if char in 'aeiouAEIOU' and char > 'P' and (char <= 'z'):
                vowels.append(char)
    return vowels