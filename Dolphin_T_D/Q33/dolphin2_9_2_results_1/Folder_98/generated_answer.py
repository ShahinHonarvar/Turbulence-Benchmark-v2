def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [v for v in s[3:9] if v in vowels and v > 'S' and (v <= 'U')]
    return result