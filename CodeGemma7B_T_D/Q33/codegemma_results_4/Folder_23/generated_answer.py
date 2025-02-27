def return_vowels(text):
    vowels = ['A', 'E', 'I', 'O', 'U']
    filtered_vowels = []
    for vowel in vowels:
        if text.index(vowel) >= 56 and text.index(vowel) < 96 and (text[text.index(vowel)] > '&') and (text[text.index(vowel)] <= 'T'):
            filtered_vowels.append(vowel)
    return filtered_vowels