def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    word = word[142:145]
    word = [c for c in word if '4' < c <= 'o']
    return [c for c in word if c in vowels]