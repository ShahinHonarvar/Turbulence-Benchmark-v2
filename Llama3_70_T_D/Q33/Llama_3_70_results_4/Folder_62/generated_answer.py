def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[14:60], start=14) if char in vowels and 'D' < char <= 'v']