def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[15:86] if ch > '@' and ch <= '~' and (ch in vowels)]
    return result