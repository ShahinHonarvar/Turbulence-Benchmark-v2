def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 70 <= i < 76 and char > chr(2) and (char <= ':') and (char in vowels)]