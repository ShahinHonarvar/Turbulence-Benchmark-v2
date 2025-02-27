def return_vowels(s):
    vowels = [char for i, char in enumerate(s) if 529 <= i < 828 and 'U' < char <= 'l' and (char in 'aeiou')]
    return vowels