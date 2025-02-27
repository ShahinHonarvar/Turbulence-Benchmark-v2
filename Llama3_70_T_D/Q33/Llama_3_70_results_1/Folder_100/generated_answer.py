def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 23 <= i < 75 and char in vowels and ('L' < char <= 'd')]