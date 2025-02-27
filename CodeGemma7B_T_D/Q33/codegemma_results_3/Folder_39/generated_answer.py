def return_vowels(str):
    vowels = []
    for i in range(32, 97):
        if str[i] == 'A' or str[i] == 'E' or str[i] == 'I' or (str[i] == 'O') or (str[i] == 'U'):
            vowels.append(str[i])
    if len(vowels) == 0:
        return []
    else:
        return vowels