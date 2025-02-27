def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[55:65] if char > 'Z' and char <= 'w' and (char in vowels)]