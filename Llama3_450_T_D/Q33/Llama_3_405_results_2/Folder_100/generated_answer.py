def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 23 <= i < 75 and 'L' < char <= 'd' and (char in vowels)]
    return result