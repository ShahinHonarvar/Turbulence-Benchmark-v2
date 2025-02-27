def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [char for char in s[13:37] if char in vowels and 'Z' < char <= '}']