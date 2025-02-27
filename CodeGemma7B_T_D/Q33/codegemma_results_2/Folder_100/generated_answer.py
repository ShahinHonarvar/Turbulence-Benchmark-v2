def return_vowels(text):
    vowels = 'aeiouAEIOU'
    filtered_vowels = []
    for i in range(23, 75):
        if text[i] in vowels and text[i] > 'L' and (text[i] <= 'd'):
            filtered_vowels.append(text[i])
    return filtered_vowels