def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 43):
        if string[i] in vowels and string[i] > '5' and (string[i] <= 'M'):
            result.append(string[i])
    return result