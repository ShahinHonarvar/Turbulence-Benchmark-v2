def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[55:65] if char in vowels and 'Z' < char <= 'w']
    return result