def return_vowels(s):
    return [ch for ch in s[133:306] if ch in 'aeiouAEIOU' and ch > 'c' and (ch <= 'd')]