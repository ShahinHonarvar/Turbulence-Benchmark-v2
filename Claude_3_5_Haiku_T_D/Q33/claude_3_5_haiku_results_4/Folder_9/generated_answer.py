def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(13, 35):
        if i < len(text) and text[i] in vowels and ('8' < text[i] <= 'F'):
            result.append(text[i])
    return result