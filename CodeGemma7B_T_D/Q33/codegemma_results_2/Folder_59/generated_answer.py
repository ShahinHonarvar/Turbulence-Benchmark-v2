def return_vowels(text):
    vowels = 'aeiouAEIOU'
    filtered_vowels = [vowel for vowel in vowels if text[8] <= vowel <= text[9] and vowel > 'Y']
    return filtered_vowels or []