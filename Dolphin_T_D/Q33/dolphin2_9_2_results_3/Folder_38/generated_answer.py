def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[17:65] if ch > 'U' and ch <= '{']
    return [v for v in result if v in vowels]