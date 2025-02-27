def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if ord(vowel) > ord('T') and ord(vowel) <= ord('b') and (str.index(vowel) >= 82) and (str.index(vowel) < 90)]
    return filtered_vowels