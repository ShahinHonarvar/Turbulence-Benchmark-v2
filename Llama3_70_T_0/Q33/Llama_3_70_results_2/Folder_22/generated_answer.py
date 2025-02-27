def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 56 <= i < 90 and char > 'K' and (char <= 'z') and (char in vowels)]