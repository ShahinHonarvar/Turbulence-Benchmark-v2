def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 82 <= i < 90 and char > 'T' and (char <= 'b') and (char in vowels)]