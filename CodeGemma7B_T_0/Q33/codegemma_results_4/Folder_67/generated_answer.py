def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[21:59] if char in vowels and char > '/' and (char <= 'a')]