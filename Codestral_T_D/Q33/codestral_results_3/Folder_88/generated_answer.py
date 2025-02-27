def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[70:76] if char in vowels and char > chr(2) and (char <= chr(58))]