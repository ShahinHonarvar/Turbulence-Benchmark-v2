def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s) if 19 <= i < 32 and char in vowels and ('0' < char <= '7')]