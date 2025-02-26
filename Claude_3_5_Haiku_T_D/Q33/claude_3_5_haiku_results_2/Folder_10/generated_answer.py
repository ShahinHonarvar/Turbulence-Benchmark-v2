def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[31:37] if char in vowels and ord(';') < ord(char) <= ord('t')]
    return result