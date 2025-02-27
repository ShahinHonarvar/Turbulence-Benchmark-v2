def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[22:82]) if char in vowels and 'N' < char <= 'o']
    return result