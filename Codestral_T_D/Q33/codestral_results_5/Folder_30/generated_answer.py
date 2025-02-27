def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [ch for ch in s[11:61] if ch in vowels and 'M' < ch <= 'W']