def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [i for i in str[51:77] if i in vowels and ord(i) > 4 and (ord(i) <= 97)]