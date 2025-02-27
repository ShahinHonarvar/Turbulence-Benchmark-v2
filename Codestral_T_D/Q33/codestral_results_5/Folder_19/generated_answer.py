def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[51:77] if ch in vowels and ord(ch) > 4 and (ord(ch) <= 61)]