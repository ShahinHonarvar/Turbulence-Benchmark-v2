def return_vowels(string):
    vowels = list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'] and 10 <= string.index(x) <= 81 and (x > '$') and (x <= '@'), string))
    return vowels