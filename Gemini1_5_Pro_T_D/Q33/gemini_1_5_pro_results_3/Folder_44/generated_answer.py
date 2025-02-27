def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(46, 49):
        if i < len(text) and text[i] in vowels and (text[i] > '[') and (text[i] <= 'p'):
            result.append(text[i])
    return result