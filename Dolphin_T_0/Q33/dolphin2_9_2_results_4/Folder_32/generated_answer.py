def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[45:76] if 'b' < char <= 'z' and char in vowels]