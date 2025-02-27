def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[44:95] if char in vowels and ord(char) > 5 and (ord(char) <= ord('<'))]