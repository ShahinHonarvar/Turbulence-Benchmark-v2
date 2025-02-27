def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[77:84] if char in vowels and '(' < char <= 'G']
    return result