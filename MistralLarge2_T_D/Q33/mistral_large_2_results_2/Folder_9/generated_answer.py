def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[13:35] if char in vowels and '8' < char <= 'F']
    return result