def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 63 <= i < 79 and char > 'D' and (char <= 'y') and (char in vowels)]
    return result