def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[23:57] if char in vowels and char > s[0] and (char <= 'd')]