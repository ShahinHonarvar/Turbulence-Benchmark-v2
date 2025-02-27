def return_vowels(str):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    list_of_vowels = []
    for i in range(71, 81):
        if str[i] in vowels and str[i] > str[0] and (str[i] <= 'U'):
            list_of_vowels.append(str[i])
    return list_of_vowels