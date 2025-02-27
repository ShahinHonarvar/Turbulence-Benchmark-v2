def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[1:7] if char in vowels and 'F' < char <= 'j']