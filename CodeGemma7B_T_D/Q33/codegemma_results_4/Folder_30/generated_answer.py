def return_vowels(s):
    vowels = 'AEIOUaeiou'
    filtered_vowels = [vowel for vowel in vowels[11:61] if vowel not in 'MNPQRSTUVWXYZ' and vowel in 'MW']
    return filtered_vowels