def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[43:70] if char in vowels and '*' < char <= 'b']
    return result