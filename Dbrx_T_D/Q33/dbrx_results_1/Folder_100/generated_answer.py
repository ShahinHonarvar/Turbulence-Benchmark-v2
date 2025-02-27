def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[23:75] if char > 'L' and char <= 'd' and (char in vowels)]