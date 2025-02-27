def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [v for v in vowels if v > s[65] and v <= s[67]]
    return result