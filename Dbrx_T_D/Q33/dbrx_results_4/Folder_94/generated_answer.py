def return_vowels(s):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    return [char for char in s[40:94] if char in vowels and ord('4') < ord(char) <= ord('H')]