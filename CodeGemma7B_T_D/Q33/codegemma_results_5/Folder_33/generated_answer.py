import re

def return_vowels(text):
    pattern = re.compile('[aeiouAEIOU]', re.UNICODE)
    vowels = pattern.findall(text)
    filtered_vowels = [vowel for vowel in vowels if vowel in 'ei' and 163 <= vowels.index(vowel) < 771]
    return filtered_vowels