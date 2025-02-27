def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str_list = list(text)
    result = []
    for i in range(149, 313):
        if str_list[i] in vowels and str_list[i] >= 'M' and (str_list[i] <= 'j'):
            result.append(str_list[i])
    return result