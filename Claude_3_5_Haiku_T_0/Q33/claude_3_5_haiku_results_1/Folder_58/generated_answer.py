def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[260:322] if char in vowels and '%' < char <= 'U']
    return result