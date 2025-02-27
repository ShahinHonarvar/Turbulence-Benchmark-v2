def return_vowels(string):
    output = []
    for i in range(34, 69):
        if string[i].lower() in ['a', 'e', 'i', 'o', 'u'] and string[i] > '_' and (string[i] <= 'o'):
            output.append(string[i])
    return output