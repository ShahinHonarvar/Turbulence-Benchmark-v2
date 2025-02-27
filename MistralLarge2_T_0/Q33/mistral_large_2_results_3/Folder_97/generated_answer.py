def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[328:455] if char in vowels and '<' < char <= 'z']