def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(string) if 29 <= i < 73 and '#' < char <= '.' and (char in vowels)]