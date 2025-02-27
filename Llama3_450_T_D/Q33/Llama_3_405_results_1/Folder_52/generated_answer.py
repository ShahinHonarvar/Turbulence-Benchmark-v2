def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 24 <= i < 68 and char in vowels and ('f' < char <= '|')]
    return result