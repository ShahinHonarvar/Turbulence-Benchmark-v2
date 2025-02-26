def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(55, 65):
        if i < len(string):
            if string[i] in vowels and 'Z' < string[i] <= 'w':
                result.append(string[i])
    return result