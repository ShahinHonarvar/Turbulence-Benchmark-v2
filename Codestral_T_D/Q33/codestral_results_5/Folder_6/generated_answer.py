def return_vowels(string):
    vowels = ['a', 'e', 'i']
    result = []
    for i in range(20, 34):
        if i < len(string) and string[i] > 'U' and (string[i] <= 'i') and (string[i] in vowels):
            result.append(string[i])
    return result