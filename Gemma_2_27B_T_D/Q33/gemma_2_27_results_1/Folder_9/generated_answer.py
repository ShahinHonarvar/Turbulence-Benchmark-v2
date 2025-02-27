def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(13, 35):
        if i < len(text) and text[i] in vowels and (chr(8) < text[i] <= chr(70)):
            result.append(text[i])
    return result