def return_vowels(text):
    vowels = []
    for i in range(770, 852):
        if i < len(text):
            char = text[i]
            if char in 'aeiouAEIOU' and char > 'B' and (char <= 'i'):
                vowels.append(char)
    return vowels