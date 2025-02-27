def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[171:402] if ch > 'I' and ch <= 'k' and (ch in vowels)]