def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[74:96] if char in vowels and 'I' < char <= 'X']
    return result