def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[54:82]) if char in vowels and '=' < char <= '@']
    return result