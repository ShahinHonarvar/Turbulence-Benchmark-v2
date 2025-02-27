def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[31:37] if char in vowels and ';' < char <= 't']
    return result