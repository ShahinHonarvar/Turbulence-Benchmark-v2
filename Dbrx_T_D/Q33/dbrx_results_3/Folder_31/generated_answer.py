def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [vowel for vowel in vowels if 65 <= ord(vowel) < 70 and '%' < vowel <= 'G']
    return result