def return_vowels(text):
    vowels = []
    for i in range(24, 68):
        if i < len(text):
            char = text[i]
            if char in 'aeiouAEIOU' and 'f' < char <= '|':
                vowels.append(char)
    return vowels