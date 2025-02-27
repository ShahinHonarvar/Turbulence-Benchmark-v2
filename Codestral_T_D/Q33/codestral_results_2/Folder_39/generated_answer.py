def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [ch for ch in s[32:97] if ch > 'Q' and ch <= ']' and (ch in vowels)]