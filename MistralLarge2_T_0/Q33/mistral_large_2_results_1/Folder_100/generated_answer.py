def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[23:75] if char in vowels and 'L' < char <= 'd']