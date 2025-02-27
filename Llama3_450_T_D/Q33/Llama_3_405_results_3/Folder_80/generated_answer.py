def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[85:99]) if char in vowels and '/' < char <= 'n']
    return result