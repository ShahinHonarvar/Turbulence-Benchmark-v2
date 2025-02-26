def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[17:65] if char in vowels and 'U' < char <= '{']
    return result