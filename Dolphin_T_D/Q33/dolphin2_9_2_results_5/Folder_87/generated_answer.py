def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[34:58] if ch > 'b' and ch <= 'o' and (ch in vowels)]