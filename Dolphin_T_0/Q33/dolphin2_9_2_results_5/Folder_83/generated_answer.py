def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[90:97] if char in vowels and '__' < char <= 'x']
    return result