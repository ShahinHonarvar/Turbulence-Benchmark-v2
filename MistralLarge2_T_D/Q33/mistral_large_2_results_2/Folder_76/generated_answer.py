def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[495:837] if char in vowels and 'B' < char <= 't']