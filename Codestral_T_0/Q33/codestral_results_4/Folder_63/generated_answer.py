def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o']
    return [char for char in s[34:69] if char in vowels and char > '_' and (char <= 'o')]