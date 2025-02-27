def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[23:85] if char in vowels and char > 'W' and (char <= 'v')]