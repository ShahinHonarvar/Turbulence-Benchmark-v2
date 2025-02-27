def return_vowels(text):
    vowels = []
    for i in range(133, 306):
        if i < len(text) and text[i] in 'aeiouAEIOU' and ('c' < text[i] <= 'd'):
            vowels.append(text[i])
    return vowels