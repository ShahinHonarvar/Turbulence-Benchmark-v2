def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o']
    return [char for char in s[17:65] if char in vowels and char > 'u' and (char <= '{')]