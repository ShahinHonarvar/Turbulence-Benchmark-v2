def return_vowels(s):
    return [ch for ch in s[64:82] if ch > 'P' and ch <= 'z' and (ch.lower() in 'aeiou')]