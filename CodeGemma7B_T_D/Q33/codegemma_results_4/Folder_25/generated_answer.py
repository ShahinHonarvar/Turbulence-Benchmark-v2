def return_vowels(str):
    result = []
    vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
    for i in range(28, 76):
        if str[i] in vowels and str[i] > '+' and (str[i] <= 'z'):
            result.append(str[i])
    return result