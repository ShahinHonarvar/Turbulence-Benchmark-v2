def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 47 <= i < 89 and char > '@' and (char <= 'n') and (char in vowels)]