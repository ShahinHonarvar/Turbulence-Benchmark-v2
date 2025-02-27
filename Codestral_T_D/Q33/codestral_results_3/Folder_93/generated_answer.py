def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[54:82] if char > '=' and char <= '@' and (char in vowels)]
    return result