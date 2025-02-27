def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 202 <= i < 872 and char in vowels and (3 < char <= '>')]
    return result