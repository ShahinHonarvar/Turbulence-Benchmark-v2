def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[495:837] if char in vowels and char > 'B' and (char <= 't')]