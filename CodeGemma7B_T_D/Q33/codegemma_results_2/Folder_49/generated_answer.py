def return_vowels(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel in x and vowel > 'R' and (vowel <= 'b') and (x.index(vowel) in range(10, 97))]
    return filtered_vowels