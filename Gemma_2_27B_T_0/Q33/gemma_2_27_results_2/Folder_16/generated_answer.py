def return_vowels(s):
    return [char for char in s[133:306] if char in 'aeiouAEIOU' and char > 'c' and (char <= 'd')]