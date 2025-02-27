def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[47:61] if char in vowels and 9 < ord(char) <= ord('O')]