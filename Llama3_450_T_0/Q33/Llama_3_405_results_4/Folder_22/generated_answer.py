def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[56:90] if char in vowels and 'K' < char <= 'z']
    return result