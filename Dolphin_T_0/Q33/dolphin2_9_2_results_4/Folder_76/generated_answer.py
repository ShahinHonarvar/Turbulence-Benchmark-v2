def return_vowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    characters = string[495:837]
    result = [char for char in characters if 'B' < char <= 't' and char in vowels]
    return result