def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[24:59] if char in vowels and char > 'N' and (char <= 'U')]