def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(90, 97):
        if str[i] in vowels and str[i] > '_' and (str[i] <= 'x'):
            result.append(str[i])
    return result