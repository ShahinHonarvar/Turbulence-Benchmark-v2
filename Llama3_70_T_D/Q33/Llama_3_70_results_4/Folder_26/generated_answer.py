def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 10 <= i < 82 and char > '$' and (char <= '@') and (char in vowels)]