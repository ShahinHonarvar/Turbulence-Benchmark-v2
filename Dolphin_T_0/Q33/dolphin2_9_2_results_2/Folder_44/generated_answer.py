def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [text[i] for i in range(46, 49) if text[i] > '[' and text[i] <= 'p' and (text[i] in vowels)]
    return result