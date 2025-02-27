def return_vowels(arg):
    result = [i for i in arg[85:99] if i in {'a', 'e', 'i', 'o', 'u'} and i > '/' and (i <= 'n')]
    return result