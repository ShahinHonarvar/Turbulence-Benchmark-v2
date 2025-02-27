def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[149:313] if char in vowels and 'M' < char <= 'j']