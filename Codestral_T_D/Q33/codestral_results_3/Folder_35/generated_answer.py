def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[483:664] if char in vowels and '&' < char <= 'h']