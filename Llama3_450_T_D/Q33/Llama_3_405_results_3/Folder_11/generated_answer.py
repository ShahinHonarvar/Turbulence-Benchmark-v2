def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for idx, char in enumerate(s) if 29 <= idx < 73 and '#' < char <= '.' and (char in vowels)]