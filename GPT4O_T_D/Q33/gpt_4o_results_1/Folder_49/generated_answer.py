def return_vowels(s):
    return [char for char in s[10:97] if char in 'aeiouAEIOU' and 'R' < char <= 'b']