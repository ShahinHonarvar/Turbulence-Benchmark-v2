def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[21:23] if char in vowels and '-' < char <= 'n']
    return result