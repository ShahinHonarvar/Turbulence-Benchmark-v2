def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [v for v in vowels if 'p' >= v > '<' and 19 <= s.index(v) < 20]