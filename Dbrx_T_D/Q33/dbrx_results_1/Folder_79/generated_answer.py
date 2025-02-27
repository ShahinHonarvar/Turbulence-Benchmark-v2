def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[74:96] if char > 'I' and char <= 'X' and (char in vowels)]