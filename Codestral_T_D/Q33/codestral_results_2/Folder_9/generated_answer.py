def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[13:35] if char in vowels and char > chr(8) and (char <= chr(15))]