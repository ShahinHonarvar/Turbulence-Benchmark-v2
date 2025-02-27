def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    characters = s[163:771]
    result = [c for c in characters if c > ':' and c <= 'E' and (c in vowels)]
    return result