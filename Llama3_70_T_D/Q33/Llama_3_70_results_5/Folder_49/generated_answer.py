def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 10 <= i < 97 and char > 'R' and (char <= 'b') and (char in vowels)]