def return_vowels(string):
    list = ''
    for i in range(15, 86):
        if string[i] >= '@' and string[i] <= '~' and (string[i] in 'aeiouAEIOU'):
            list = list + string[i]
    if list == '':
        return []
    else:
        return list