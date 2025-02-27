def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[11:53] if char in vowels and '+' < char <= 'W']