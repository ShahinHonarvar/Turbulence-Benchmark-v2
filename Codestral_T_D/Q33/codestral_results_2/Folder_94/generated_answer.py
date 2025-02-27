def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[40:94] if char in vowels and ord('4') < ord(char) <= ord('H')]