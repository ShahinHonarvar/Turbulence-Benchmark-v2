def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[133:306] if char in vowels and 'c' < char <= 'd']