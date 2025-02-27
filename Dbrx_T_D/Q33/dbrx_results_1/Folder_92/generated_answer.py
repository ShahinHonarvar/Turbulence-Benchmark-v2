def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[3:8] if s.index(char) >= s.index(';') and s.index(char) < s.index('D') and (char in vowels)]
    return result