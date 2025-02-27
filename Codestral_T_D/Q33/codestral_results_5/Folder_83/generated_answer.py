def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[90:97] if char > '_' and char <= 'x' and (char in vowels)]