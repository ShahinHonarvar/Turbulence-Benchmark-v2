def return_vowels(str):
    vowels = list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'] and x in str and (str.index(x) >= 70) and (str.index(x) < 76) and (ord(x) > ord(2)) and (ord(x) <= ord('.')), str))
    return vowels