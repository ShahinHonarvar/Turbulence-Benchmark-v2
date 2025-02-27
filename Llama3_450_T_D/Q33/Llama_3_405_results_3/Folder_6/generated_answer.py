def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 20 <= i < 34 and char in vowels and ('U' < char <= 'i')]