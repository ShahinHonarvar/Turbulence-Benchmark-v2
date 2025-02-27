def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[10:97] if char > 'R' and char <= 'b' and (char in vowels)]