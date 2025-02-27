def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[19:32] if char in vowels and 0 < ord(char) <= 7]
    return result