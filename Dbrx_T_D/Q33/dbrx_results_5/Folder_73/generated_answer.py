def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(string)):
        if string[i] >= '@' and string[i] <= 'n' and (i >= 47) and (i < 89):
            if string[i] in vowels:
                result.append(string[i])
    return result