def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[23:57] if char in vowels and '0' < char <= 'd']
    return result