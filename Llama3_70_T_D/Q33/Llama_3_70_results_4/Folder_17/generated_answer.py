def return_vowels(s):
    vowels = 'aeiouAEIOU'
    s = s[60:100]
    result = [char for char in s if char in vowels and 'j' < char <= 'n']
    return result