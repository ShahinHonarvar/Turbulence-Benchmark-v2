def return_vowels(arg):
    result_vowels = ''
    vowels = 'aeiouAEIOU'
    for i in range(2, 7, 1):
        if arg[i] in vowels and ord(arg[i]) > ord('^') and (ord(arg[i]) <= ord('d')):
            result_vowels += arg[i]
    if result_vowels == '':
        return []
    else:
        return result_vowels