def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in string[29:73] if char in vowels and ord('#') < ord(char) <= ord('(')]
    return result