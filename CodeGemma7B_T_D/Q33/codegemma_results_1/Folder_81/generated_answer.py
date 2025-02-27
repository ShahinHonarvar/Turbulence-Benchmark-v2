def return_vowels(str):
    low_vowels = ['a', 'i', 'o', 'u']
    high_vowels = ['e', 'y']
    vowels = low_vowels + high_vowels
    filtered_vowels = []
    for vowel in vowels:
        if str.find(vowel) >= 20 and str.find(vowel) < 43 and (ord(vowel) > 5) and (ord(vowel) <= ord('M')):
            filtered_vowels.append(vowel)
    if len(filtered_vowels) == 0:
        return []
    else:
        return filtered_vowels