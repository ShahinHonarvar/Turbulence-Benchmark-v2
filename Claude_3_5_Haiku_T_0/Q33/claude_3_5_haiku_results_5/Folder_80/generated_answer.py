def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[85:99] if char in vowels and '/' < char <= 'n']
    return result