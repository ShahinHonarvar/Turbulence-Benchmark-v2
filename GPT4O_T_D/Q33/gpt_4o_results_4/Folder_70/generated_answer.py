def return_vowels(s):
    if len(s) < 172:
        return []
    return [ch for ch in s[171:402] if ch in 'aeiou' and 'I' < ch <= 'k']