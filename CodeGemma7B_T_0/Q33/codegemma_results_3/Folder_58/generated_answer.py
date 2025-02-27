def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(260, 322):
        if text[i] in vowels and text[i] > '%' and (text[i] <= 'U'):
            result.append(text[i])
    return result