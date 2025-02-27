def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[273:275] if char > '+' and char <= 'o' and (char in vowels)]