def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i in range(55, 65):
        for vowel in vowels:
            if text[i] == vowel and vowel > 'Z' and (vowel <= 'w'):
                filtered_vowels.append(vowel)
    return filtered_vowels