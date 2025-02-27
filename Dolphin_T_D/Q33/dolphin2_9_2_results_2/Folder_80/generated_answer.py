def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [c for c in s[85:99] if c > '/' and c <= 'n' and (c in vowels)]
    return result