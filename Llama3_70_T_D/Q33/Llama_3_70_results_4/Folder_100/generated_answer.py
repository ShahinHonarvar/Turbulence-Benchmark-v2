def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[23:75]) if char in vowels and 'L' < char <= 'd']