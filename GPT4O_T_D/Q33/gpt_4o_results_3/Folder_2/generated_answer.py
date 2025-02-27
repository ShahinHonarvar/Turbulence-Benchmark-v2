def return_vowels(s):
    vowels = 'aeiouAEIOU'
    start, end = (170, 645)
    return [char for char in s[start:end] if char in vowels and 'E' < char <= '~']