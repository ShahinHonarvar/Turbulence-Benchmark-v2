def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[5:7] if char in vowels and ord(char) > 3 and (ord(char) <= ord('^'))]