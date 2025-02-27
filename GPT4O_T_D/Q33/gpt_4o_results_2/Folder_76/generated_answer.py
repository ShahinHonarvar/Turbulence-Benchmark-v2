def return_vowels(s):
    vowels = set('aeiouAEIOU')
    result = [char for char in s[495:837] if char in vowels and 'B' < char <= 't']
    return result