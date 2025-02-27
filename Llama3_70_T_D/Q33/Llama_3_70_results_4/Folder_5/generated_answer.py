def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 44 <= i < 95 and char > '5' and (char <= '<') and (char in vowels)]