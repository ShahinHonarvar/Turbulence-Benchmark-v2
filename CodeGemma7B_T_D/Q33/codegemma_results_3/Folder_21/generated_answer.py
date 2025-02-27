def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    ret = []
    for i in range(574 - 4 - 1):
        if str[464 + i] in vowels and str[464 + i] >= 'a' and (str[464 + i] <= 'g'):
            ret.append(str[464 + i])
    return ret