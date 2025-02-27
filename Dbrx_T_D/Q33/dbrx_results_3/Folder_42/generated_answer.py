def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[12:39:1] if s.index(char) > s.index(';') and s.index(char) <= s.index('|') and (char in vowels)]