def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[56:96] if char in vowels and '&' < char <= 'T']
    return result