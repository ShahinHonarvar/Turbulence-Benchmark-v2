def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    list_ = []
    for vowel in vowels:
        if vowel > '_' and vowel <= 'x' and (word.find(vowel) >= 90) and (word.find(vowel) < 97):
            list_.append(vowel)
    return list_