def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[20:41] if char in vowels and 'K' < char <= 'Z']