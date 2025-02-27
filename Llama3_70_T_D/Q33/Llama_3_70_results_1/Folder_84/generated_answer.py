def return_vowels(s):
    vowels = [char for i, char in enumerate(s) if 770 <= i < 852 and 'B' < char <= 'i' and (char in 'aeiou')]
    return vowels