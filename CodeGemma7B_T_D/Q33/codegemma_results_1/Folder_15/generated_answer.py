def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[5:6] if char in vowels and 3 < char <= '^']
    return result