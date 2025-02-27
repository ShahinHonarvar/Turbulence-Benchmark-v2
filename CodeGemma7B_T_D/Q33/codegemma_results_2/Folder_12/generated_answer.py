def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(13, 37):
        if string[i] in vowels and string[i] >= '{' and (string[i] <= '}'):
            result.append(string[i])
    return result