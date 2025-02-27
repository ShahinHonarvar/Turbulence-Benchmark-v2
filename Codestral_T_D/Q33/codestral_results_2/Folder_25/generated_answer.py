def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(28, 76):
        if string[i] > '+' and string[i] <= 'z' and (string[i] in vowels):
            result.append(string[i])
    return result