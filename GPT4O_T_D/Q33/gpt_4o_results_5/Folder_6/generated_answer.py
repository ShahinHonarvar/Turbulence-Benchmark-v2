def return_vowels(s):
    vowels = set('aeiouAEIOU')
    return [ch for ch in s[20:34] if ch in vowels and 'U' < ch <= 'i']