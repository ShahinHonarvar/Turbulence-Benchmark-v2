def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in string[22:82] if 'n' < c <= 'o' and c in vowels]
    return result