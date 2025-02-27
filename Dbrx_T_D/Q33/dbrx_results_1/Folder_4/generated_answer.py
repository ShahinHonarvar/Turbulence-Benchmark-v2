def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[40:91] if char.lower() in vowels and char > 'A' and (char <= 'x')]
    return result