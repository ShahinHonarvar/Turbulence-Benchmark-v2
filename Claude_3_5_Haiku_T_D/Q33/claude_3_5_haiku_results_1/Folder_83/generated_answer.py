def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string if char in vowels and 90 <= ord(char) <= 97 and ('_' < char <= 'x')]
    return result