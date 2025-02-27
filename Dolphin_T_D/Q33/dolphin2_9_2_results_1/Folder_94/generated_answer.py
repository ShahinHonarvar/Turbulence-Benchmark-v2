def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(40, 94):
        if string[i] > '4' and string[i] <= 'H':
            if string[i] in vowels:
                result.append(string[i])
    return result