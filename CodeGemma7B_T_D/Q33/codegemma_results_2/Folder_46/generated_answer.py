def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(10, 83):
        if str[i] in vowels and str[i] > '%' and (str[i] <= 'e'):
            result.append(str[i])
    return result