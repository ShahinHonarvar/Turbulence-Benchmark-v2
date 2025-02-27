def return_vowels(str):
    vowels = ['o', 'u', 'e', 'i', 'a']
    return_vowels = []
    for i in range(142, 145):
        if str[i] in vowels and ord(str[i]) > 4 and (ord(str[i]) <= ord('o')):
            return_vowels.append(str[i])
    return return_vowels or ['']