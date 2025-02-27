def return_vowels(characters):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for vowel in vowels:
        if characters[11:].find(vowel) >= 11 and characters.find(vowel) <= 53 and (characters[11:].find(vowel) > characters.find('+')) and (characters.find(vowel) <= characters.find('W')):
            filtered_vowels.append(vowel)
    return filtered_vowels