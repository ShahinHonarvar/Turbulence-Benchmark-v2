def return_vowels(text):
    vowels = []
    for i in range(90, 97):
        if i >= len(text):
            break
        char = text[i]
        if char in 'aeiouAEIOU' and '_' < char <= 'x':
            vowels.append(char)
    return vowels