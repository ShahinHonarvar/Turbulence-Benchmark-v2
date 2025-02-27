def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[64:82] if char in vowels and 'P' < char <= 'z']
    return result