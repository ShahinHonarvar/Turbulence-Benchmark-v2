def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(8, 9):
        if string[i] in vowels and string[i] > 'Y' and (string[i] <= 's'):
            result.append(string[i])
    return result