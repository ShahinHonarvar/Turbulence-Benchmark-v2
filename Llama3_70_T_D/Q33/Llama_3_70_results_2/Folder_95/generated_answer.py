def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 32 <= i < 61 and char > '?' and (char <= 'P') and (char in vowels)]