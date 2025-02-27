def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(3, 8):
        if str[i] in vowels and str[i] > ';' and (str[i] <= 'D'):
            result.append(str[i])
    return result