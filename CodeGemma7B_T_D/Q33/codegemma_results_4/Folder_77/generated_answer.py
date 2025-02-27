def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(837, 975):
        if str[i] in vowels and str[i] > 'N' and (str[i] <= 'W'):
            result.append(str[i])
    return result