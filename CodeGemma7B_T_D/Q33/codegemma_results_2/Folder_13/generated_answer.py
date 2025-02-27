def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i in range(149, 313):
        if str[i] in vowels and str[i] > 'M' and (str[i] <= 'j'):
            filtered_vowels.append(str[i])
    return filtered_vowels