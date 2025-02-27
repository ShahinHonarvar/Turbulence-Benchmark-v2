def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[24:64] if char in vowels and 'F' < char <= 'h']