def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[90:97] if char in vowels and '_' < char <= 'x']
    return result