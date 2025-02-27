def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[5:6] if char in vowels and char > '3' and (char <= '^')]