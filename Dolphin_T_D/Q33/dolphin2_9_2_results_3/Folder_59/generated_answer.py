def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[8:9] if char in vowels and char > 'Y' and (char <= 's')]