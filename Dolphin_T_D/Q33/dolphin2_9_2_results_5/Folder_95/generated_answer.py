def return_vowels(s):
    return [ch for ch in s[32:61] if ch > '?' and ch <= 'P' and (ch.lower() in 'aeiou')]