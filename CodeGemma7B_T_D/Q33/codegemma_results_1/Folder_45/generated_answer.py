def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i in range(43, 70):
        if str[i] in vowels and str[i] > '*' and (str[i] <= 'b'):
            filtered_vowels.append(str[i])
    return filtered_vowels