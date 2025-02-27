def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[604:949] if char in vowels and 'N' < char <= 'U']