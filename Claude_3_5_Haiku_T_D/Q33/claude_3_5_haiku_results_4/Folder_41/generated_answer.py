def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[71:81] if char in vowels and '>' < char <= 'U']