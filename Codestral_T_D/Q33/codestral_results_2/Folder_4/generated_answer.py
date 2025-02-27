def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[40:91] if char > 'A' and char <= 'x' and (char in vowels)]