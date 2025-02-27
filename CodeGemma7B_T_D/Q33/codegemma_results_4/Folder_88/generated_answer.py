def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(70, 76):
        if str[i] in vowels and str[i] > '2' and (str[i] <= ':'):
            result.append(str[i])
    return result