def return_vowels(s):
    vowels = [char for i, char in enumerate(s) if 10 <= i < 83 and '%' < char <= 'e' and (char in 'aeiou')]
    return vowels