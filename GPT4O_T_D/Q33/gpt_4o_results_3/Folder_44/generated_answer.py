def return_vowels(s):
    vowels = set('aeiou')
    return [char for char in s[46:49] if char in vowels and ord(char) > ord('[') and (ord(char) <= ord('p'))]