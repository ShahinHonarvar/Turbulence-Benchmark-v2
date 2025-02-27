def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[495:837] if char > 'B' and char <= 't' and (char in vowels)]
    return result