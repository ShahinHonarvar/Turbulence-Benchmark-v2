def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[1:4] if char in vowels and 'C' < char <= 'I']
    return result