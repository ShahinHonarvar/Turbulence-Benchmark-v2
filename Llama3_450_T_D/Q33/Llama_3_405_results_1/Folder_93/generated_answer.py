def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[54:82] if char in vowels and '=' < char <= '@']
    return result