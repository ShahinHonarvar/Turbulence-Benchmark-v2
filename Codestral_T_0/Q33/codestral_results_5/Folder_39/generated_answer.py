def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[32:97] if char > 'Q' and char <= ']' and (char in vowels)]