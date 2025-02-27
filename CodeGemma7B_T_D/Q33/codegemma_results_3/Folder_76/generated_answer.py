def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for i in range(495, 837):
        if text[i] in vowels and text[i] > 'B' and (text[i] <= 't'):
            output.append(text[i])
    return output