def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[23:38] if char in vowels and 'N' < char <= 'k']
    return result