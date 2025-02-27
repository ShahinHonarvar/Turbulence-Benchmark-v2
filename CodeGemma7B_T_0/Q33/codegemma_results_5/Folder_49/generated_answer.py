def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(10, 97):
        if text[i] in vowels and text[i] > 'R' and (text[i] <= 'b'):
            result.append(text[i])
    return result