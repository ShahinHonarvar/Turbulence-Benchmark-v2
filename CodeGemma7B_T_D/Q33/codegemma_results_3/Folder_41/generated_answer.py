def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(71, 81):
        if string[i] in vowels and string[i] > character and (string[i] <= 'U'):
            result.append(string[i])
    return result