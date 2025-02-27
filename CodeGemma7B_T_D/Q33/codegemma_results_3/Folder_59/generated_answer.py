def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(8, 9):
        if str[i] in vowels and str[i] > 'Y' and (str[i] <= 's'):
            result.append(str[i])
    return result if result else []