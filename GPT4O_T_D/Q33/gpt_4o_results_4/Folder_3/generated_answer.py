def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[50:77] if char in vowels and '#' < char <= 'r']
    return result