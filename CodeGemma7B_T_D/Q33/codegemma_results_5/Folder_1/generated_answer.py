def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    matching_vowels = []
    for vowel in vowels:
        if vowel in string[24:64] and vowel > 'F' and (vowel <= 'h'):
            matching_vowels.append(vowel)
    return matching_vowels