def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [ch for ch in s[21:59] if ch in vowels and '/' < ch <= 'a']