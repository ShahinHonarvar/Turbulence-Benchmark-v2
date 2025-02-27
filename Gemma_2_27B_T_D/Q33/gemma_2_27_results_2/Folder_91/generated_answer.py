def return_vowels(s):
    return [char for char in s[4:8] if char in 'aeiouAEIOU' and char > 'P' and (char <= 'r')]