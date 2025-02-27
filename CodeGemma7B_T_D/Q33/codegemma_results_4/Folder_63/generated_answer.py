def return_vowels(str):
    lis = []
    for i in range(34, 69):
        if str[i] <= 'o' and ord(str[i]) > ord('_'):
            lis.append(str[i])
    if lis == []:
        return []
    else:
        return lis