def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[46:49] if char > '[' and char <= 'p' and (char in vowels)]
    return result