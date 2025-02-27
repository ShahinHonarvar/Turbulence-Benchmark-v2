def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 43 <= i < 70 and char in vowels and ('*' < char <= 'b')]