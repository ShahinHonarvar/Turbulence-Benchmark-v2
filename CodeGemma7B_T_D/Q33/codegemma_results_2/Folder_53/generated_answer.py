def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chosen_vowels = [v for v in vowels if v not in word and v > vowels[4] and (v <= vowels[10])]
    return chosen_vowels