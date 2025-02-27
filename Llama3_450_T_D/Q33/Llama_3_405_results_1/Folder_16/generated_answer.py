def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[133:306]) if char in vowels and 'c' < char <= 'd']