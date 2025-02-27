def return_vowels(s):
    return [ch for ch in s[13:35] if 8 < ord(ch) <= ord('F') and ch.lower() in 'aeiou']