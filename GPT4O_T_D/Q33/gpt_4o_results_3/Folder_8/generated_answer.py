def return_vowels(s):
    vowels = 'aeiouAEIOU'
    if len(s) < 65:
        return []
    return [char for char in s[64:82] if char in vowels and 'P' < char <= 'z']