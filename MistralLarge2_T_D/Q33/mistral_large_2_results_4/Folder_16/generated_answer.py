def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [ch for ch in s[133:306] if ch in vowels and 'c' < ch <= 'd']