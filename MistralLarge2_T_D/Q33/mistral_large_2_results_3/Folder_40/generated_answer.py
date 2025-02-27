def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 2 <= i < 7 and char in vowels and ('^' < char <= 'd')]