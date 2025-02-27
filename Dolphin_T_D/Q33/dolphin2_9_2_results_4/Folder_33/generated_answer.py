def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    characters = s[163:771]
    result = [c for c in characters if vowels.__contains__(c.lower()) and ':' < c <= 'E']
    return result