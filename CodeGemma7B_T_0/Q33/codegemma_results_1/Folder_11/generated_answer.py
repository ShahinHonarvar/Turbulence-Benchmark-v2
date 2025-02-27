def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(29, 73):
        if text[i] in vowels and text[i] > '#' and (text[i] <= '.'):
            result.append(text[i])
    return result