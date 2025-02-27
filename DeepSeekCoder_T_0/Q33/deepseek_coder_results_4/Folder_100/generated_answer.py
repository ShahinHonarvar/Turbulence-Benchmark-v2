def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[23:75] if char in vowels and 'L' < char <= 'd']
    return result