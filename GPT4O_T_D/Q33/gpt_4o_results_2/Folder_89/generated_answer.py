def return_vowels(s):
    if len(s) <= 50:
        return []
    return [ch for ch in s[50:51] if ch in 'aeiou' and ',' < ch <= 'v']