def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[12:39] if char in vowels and ';' < char <= '|']