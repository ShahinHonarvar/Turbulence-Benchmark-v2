def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[40:91] if char > 'A' and char <= 'x' and (char in vowels)]