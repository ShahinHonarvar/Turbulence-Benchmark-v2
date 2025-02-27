def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'f']
    return [vowel for vowel in vowels if 'a' < vowel <= 'f' and 28 < s.index(vowel) < 31]