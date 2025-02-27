def return_vowels(str_in):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_vowels = []
    for i in range(56, 90):
        if str_in[i] in vowels and ord(str_in[i]) > ord('K') and (ord(str_in[i]) <= ord('z')):
            return_vowels.append(str_in[i])
    if return_vowels == []:
        return_vowels = []
    return return_vowels