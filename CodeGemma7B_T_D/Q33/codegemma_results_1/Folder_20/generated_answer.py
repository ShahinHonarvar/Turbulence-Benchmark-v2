def return_vowels(mystr):
    vowels = ('a', 'e', 'i', 'o', 'u')
    filtered_vowels = [vowel for vowel in vowels if mystr.index(vowel) >= 59 and mystr.index(vowel) < 61 and (mystr[mystr.index(vowel)] > '+') and (mystr[mystr.index(vowel)] <= 'h')]
    return filtered_vowels