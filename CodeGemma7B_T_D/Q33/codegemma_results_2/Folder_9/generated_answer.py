def return_vowels(string):
    vowels = list('aeiouAEIOU')
    return [vowel for vowel in vowels[13:35] if vowel > chr(8) and vowel <= chr(70)]