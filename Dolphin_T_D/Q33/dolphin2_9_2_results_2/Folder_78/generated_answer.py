def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    temp = string[46:90]
    result = [i for i in temp if i > '@' and i <= '[' and (i in vowels)]
    return result