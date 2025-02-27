def return_vowels(text):
    vowels = []
    for i in range(43, 70):
        if i < len(text) and '*' < text[i] <= 'b' and (text[i] in 'aeiouAEIOU'):
            vowels.append(text[i])
    return vowels