def return_vowels(text):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(641, 872):
        if text[i] in vowels and text[i] > '>' and (text[i] <= 'q'):
            result.append(text[i])
    return result