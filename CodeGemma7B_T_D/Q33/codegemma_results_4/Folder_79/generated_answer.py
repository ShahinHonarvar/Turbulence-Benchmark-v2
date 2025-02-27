def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel in word and word.index(vowel) >= 74 and (word.index(vowel) < 96) and (word[word.index(vowel)] > 'I') and (word[word.index(vowel)] <= 'X')]
    return filtered_vowels