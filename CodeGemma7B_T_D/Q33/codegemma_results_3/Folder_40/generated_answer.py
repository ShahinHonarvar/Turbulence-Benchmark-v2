def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [x for x in vowels[2:7] for y in word and word[x] > '^' for z in word and word[x] <= 'd']