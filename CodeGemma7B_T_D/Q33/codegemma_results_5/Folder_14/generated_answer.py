def return_vowels(str):
    vowels = []
    for i in range(47, 62):
        if str[i] in 'aeiouAEIOU':
            if ord(str[i]) > 9 and ord(str[i]) <= ord('O'):
                vowels.append(str[i])
    return vowels