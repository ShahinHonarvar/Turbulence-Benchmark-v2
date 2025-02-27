def return_vowels(str):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(23, 38):
        if str[i] in vowels and ord(str[i]) > ord('N') and (ord(str[i]) <= ord('k')):
            result.append(str[i])
    return result