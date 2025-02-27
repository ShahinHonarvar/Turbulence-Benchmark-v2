def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[21:59]) if char in vowels and '/' < char <= 'a']
    return result