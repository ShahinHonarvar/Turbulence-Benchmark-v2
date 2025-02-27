def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[51:77] if 4 < ord(char) <= ord('.') and char in vowels]
    return result