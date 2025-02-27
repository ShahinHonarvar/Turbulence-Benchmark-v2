def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 11 <= i < 53 and '+' < char <= 'W' and (char in vowels)]