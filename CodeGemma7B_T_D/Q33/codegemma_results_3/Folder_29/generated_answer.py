def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for i in range(19, 20):
        if text[i] in vowels and text[i] > '<' and (text[i] <= 'p'):
            output.append(text[i])
    return output