def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[28:76] if char in vowels and '+' < char <= 'z']
    return result