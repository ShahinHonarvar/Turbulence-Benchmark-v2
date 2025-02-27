def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[10:97] if char in vowels and 'R' < char <= 'b']