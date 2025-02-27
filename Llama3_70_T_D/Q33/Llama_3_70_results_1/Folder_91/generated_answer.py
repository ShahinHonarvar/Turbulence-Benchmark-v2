def return_vowels(s):
    vowels = [char for i, char in enumerate(s) if 4 <= i < 8 and 'P' < char <= 'r' and (char in 'aeiou')]
    return vowels