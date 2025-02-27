def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 24 <= i < 64 and char > 'F' and (char <= 'h') and (char in vowels)]