def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[495:837]) if char in vowels and 'B' < char <= 't']
    return result