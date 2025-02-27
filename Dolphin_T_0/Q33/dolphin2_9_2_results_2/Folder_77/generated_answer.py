def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for i in range(837, 975):
        if string[i] in vowels and string[i] > 'n' and (string[i] <= 'w'):
            output.append(string[i])
    return output