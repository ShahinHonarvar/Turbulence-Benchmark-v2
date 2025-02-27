def return_vowels(s):
    vowels = [char for i, char in enumerate(s) if 27 <= i < 57 and 'o' < char <= 'w' and (char in 'aeiou')]
    return vowels