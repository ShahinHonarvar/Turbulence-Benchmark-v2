def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[19:32] if char in vowels and ord(char) > 0 and (ord(char) <= 7)]