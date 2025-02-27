def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(71, 88):
        if string[i] in vowels and string[i] > '9' and (string[i] <= 'P'):
            result.append(string[i])
    return result