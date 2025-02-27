def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for vowel in vowels:
        if 'Y' < vowel <= 's' and 8 <= s.index(vowel) < 9:
            result.append(vowel)
    return result