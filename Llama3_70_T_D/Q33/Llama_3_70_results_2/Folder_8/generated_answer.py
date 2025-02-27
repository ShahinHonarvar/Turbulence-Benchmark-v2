def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 64 <= i < 82 and char > 'P' and (char <= 'z') and (char in vowels)]