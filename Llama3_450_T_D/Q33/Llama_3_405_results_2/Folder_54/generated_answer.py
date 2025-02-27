def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[23:85]) if char in vowels and 'W' < char <= 'v']