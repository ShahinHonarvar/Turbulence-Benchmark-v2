def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[1:4] if char in vowels and 'C' < char <= 'I']