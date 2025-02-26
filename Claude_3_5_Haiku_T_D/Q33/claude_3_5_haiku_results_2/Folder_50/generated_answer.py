def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(11, 53):
        if i < len(string) and string[i] in vowels and (string[i] > '+') and (string[i] <= 'W'):
            result.append(string[i])
    return result