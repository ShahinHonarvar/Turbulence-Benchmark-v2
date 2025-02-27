def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[24:64]) if char in vowels and 'F' < char <= 'h']