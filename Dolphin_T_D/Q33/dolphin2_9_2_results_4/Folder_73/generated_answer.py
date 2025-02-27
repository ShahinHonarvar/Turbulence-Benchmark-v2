def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = string[47:89]
    result = [char for char in chars if '@' < char <= 'n' and char in vowels]
    return result