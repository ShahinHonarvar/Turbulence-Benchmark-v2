def return_vowels(string):
    vowels = list('aeiouAEIOU')
    result = []
    for i in range(34, 69):
        if i < len(string) and string[i] in vowels and ('_' < string[i] <= 'o'):
            result.append(string[i])
    return result