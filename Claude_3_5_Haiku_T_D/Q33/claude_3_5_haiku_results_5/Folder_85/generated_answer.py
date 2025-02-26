def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[55:65] if char.lower() in vowels and 'Z' < char <= 'w']
    return result