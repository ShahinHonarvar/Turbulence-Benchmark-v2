def return_vowels(s):
    return [char for char in s[2:7] if char in 'aeiouAEIOU' and '^' < char <= 'd']