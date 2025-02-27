def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [ch for ch in s[14:60] if ch in vowels and 'D' < ch <= 'v']
    return result