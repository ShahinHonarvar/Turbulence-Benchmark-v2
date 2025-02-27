def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[770:852] if char in vowels and 'B' < char <= 'i']