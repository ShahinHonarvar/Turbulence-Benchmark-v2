def return_vowels(string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for vowel in vowels:
        if vowel in string and string.index(vowel) >= 5 and (string.index(vowel) < 6) and (ord(vowel) > 3) and (ord(vowel) <= ord('^')):
            filtered_vowels.append(vowel)
    return filtered_vowels