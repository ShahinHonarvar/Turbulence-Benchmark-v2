def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 1 <= i < 5 and char in vowels and ('!' < char <= 'j')]
    return result