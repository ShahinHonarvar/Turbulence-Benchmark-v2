def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[44:95] if char in vowels and '5' < char <= '<']
    return result