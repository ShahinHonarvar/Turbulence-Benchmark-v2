def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    return [char for char in s[40:91] if char in vowels and 'A' < char <= 'x']