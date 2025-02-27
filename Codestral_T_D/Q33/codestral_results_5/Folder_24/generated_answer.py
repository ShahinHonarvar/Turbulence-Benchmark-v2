def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[23:57] if char in vowels and ord('0') < ord(char) <= ord('d')]