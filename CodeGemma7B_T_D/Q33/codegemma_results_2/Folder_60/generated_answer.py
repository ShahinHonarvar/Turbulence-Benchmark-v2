def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i in range(24, 59):
        if str[i] in vowels and str[i] > 'N' and (str[i] <= 'U'):
            filtered_vowels.append(str[i])
    return filtered_vowels