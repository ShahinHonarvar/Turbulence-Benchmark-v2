def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[41:50] if char in vowels and 'W' < char <= '[']
    return result