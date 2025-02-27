def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [v for v in vowels if v in word and 3 <= word.index(v) <= 8 and (v > 'S') and (v <= 'U')] or []