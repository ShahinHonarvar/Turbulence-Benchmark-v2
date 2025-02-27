def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 10 <= i < 82 and char in vowels and ('$' < char <= '@')]
    return result