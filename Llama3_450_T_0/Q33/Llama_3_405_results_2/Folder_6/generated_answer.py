def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[20:34] if char in vowels and 'U' < char <= 'i']