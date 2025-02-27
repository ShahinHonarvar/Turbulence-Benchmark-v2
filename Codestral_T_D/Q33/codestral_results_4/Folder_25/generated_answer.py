def return_vowels(s):
    return [ch for ch in s[28:76] if ch.lower() in 'aeiou' and '+' < ch <= 'z']