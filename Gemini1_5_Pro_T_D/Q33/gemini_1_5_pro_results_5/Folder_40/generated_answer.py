def return_vowels(text):
    vowels = []
    for i in range(2, 7):
        if i < len(text):
            char = text[i]
            if char > '^' and char <= 'd' and (char in 'aeiouAEIOU'):
                vowels.append(char)
    return vowels