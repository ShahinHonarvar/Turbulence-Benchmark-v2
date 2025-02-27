def return_vowels(str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowels = []
    for i in range(641, 872):
        if str[i] in vowel:
            if str[i] > str[i + 2] and str[i] <= 'q':
                vowels.append(str[i])
    if len(vowels) == 0:
        return []
    return vowels