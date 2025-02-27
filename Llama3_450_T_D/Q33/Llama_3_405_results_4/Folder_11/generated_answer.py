def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 29 <= i < 73 and '#' < char <= '.' and (char in vowels)]
    return result