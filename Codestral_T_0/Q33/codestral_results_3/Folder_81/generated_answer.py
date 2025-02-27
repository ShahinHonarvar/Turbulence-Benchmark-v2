def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[20:43] if char in vowels and '5' < char <= 'M']