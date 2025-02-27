def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return [vowel for vowel in vowels if ord('C') < ord(vowel) <= ord('I') and s[1] < vowel < s[4]]