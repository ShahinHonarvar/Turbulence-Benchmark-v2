def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 133 <= i < 306 and char in vowels and ('c' < char <= 'd')]
    return result