def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[41:50] if char > 'W' and char.lower() in vowels and (char <= '[')]