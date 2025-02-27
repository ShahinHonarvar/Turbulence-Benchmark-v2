def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[24:64] if char > 'F' and char <= 'h' and (char in vowels)]