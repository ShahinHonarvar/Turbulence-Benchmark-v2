def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in text[11:53] if ch in vowels and ch > '+' and (ch <= 'W')]