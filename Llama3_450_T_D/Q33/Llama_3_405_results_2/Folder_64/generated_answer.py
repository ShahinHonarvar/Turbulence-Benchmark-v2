def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 1 <= i < 7 and char in vowels and ('F' < char <= 'j')]
    return result