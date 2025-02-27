def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[770:852]) if char in vowels and 'B' < char <= 'i']
    return result