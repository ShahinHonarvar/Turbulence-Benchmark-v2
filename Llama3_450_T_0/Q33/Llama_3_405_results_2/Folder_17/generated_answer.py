def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[60:99]) if char in vowels and 'j' < char <= 'n']
    return result