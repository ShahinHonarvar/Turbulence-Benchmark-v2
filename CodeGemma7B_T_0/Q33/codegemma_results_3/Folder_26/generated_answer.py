def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(10, 82):
        if str[i] in vowels and str[i] > '$' and (str[i] <= '@'):
            result.append(str[i])
    return result