def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(47, 89):
        if string[i] > '@' and string[i] <= 'n' and (string[i] in vowels):
            result.append(string[i])
    return result