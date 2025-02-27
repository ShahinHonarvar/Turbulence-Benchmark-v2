def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for vowel in vowels:
        if vowel in text and vocal > 'I' and (vowel <= 'X') and (text.index(vowel) >= 74) and (text.index(vowel) < 96):
            filtered_vowels.append(vowel)
    return filtered_vowels