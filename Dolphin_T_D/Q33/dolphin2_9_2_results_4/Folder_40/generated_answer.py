def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s for s in string[2:7] if s in vowels and '^' < s <= 'd']
    return result