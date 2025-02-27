def return_vowels(s):
    return [char for char in s[170:645] if char in 'aeiouAEIOU' and 'E' < char <= '~']