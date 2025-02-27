def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[45:76] if 'b' < char <= 'z' and char in vowels]
    return result