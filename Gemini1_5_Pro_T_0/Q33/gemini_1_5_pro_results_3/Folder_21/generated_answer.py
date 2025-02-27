def return_vowels(text):
    vowels = []
    for i in range(464, 574):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('a' < text[i] <= 'g'):
            vowels.append(text[i])
    return vowels