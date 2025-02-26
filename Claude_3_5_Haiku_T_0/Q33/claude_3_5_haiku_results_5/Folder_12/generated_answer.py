def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[13:37] if char in vowels and 'Z' < char <= '}']