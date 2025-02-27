def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s) if 69 <= i < 82 and '[' < char <= '~' and (char in vowels)]
    return result