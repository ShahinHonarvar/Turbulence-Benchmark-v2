def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [letter for letter in vowels if string[1:9].index(letter) > 0 and string[1:9].index(letter) <= string.index(k)]