def return_vowels(s):
    vowels = set('aeiou')
    result = [char for char in s[328:455] if char in vowels and '<' < char <= 'z']
    return result