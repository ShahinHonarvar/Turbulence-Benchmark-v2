def return_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for vowel in vowels:
        if vowel > 'W' and vowel <= '[':
            index = vowels.index(vowel)
            if index >= 41 and index < 50:
                result.append(vowel)
    return result