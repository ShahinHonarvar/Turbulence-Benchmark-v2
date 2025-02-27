def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[56:90] if char in vowels and char > 'k' and (char <= 'z')]