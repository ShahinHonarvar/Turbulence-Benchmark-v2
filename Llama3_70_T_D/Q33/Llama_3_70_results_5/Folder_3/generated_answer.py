def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 50 <= i < 77 and char in vowels and ('#' < char <= 'r')]