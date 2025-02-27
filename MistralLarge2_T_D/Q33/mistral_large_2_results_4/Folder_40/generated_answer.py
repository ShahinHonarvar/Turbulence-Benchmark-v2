def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[2:7] if char in vowels and '^' < char <= 'd']