def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 23 <= i < 85 and char > 'W' and (char <= 'v') and (char in vowels)]