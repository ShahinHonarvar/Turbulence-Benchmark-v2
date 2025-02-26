def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s if char in vowels and 90 <= ord(char) and (ord(char) < 97) and ('_' < char <= 'x')]
    return result