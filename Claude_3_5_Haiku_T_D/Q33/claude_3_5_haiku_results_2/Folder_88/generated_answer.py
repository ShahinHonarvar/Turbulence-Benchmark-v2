def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(70, 76):
        if i < len(string):
            if string[i] in vowels and string[i] > chr(2) and (string[i] <= chr(58)):
                result.append(string[i])
    return result