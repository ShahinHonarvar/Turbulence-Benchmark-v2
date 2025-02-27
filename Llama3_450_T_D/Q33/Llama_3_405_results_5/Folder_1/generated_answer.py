def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 24 <= i < 64 and 'F' < char <= 'h' and (char in vowels)]
    return result