def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[56:96] if char > '&' and char <= 'T' and (char in vowels)]
    return result