def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[47:89] if char in vowels and '@' < char <= 'n']
    return result