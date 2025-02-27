def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[19:20] if char in vowels and '<' < char <= 'p']
    return result