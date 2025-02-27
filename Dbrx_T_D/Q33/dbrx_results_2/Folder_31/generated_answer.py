def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [vowel for vowel in vowels if ord('A') <= ord(vowel) < ord('G') and ord('%') < ord(vowel) <= ord('G')]
    return result