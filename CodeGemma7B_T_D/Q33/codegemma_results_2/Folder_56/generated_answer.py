def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    for vowel in vowels:
        if vowel >= '@' and vowel <= '~' and (string.find(vowel) >= 15) and (string.find(vowel) < 86):
            vowels_in_range.append(vowel)
    if vowels_in_range == []:
        return []
    return vowels_in_range