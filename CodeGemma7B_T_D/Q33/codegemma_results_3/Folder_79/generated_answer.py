def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for vowel in vowels:
        if string.find(vowel) in range(74, 96) and vowel > 'I' and (vowel <= 'X'):
            result.append(vowel)
    return result