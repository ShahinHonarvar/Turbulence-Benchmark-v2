def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[10:83]) if char in vowels and '%' < char <= 'e']