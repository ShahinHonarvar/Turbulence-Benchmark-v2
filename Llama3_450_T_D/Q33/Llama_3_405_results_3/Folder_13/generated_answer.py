def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[149:313]) if char in vowels and 'M' < char <= 'j']
    return result