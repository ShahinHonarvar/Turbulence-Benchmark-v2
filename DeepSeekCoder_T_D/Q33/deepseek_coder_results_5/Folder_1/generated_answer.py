def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[24:64] if char in vowels and 'F' < char <= 'h']
    return result