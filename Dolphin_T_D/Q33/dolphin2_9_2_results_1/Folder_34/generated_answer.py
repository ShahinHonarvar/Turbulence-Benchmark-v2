def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[19:32] if ch > '0' and ch <= '7' and (ch in vowels)]
    return result