def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    relevant_chars = [c for c in s[31:37] if '>' < c <= 't']
    return [c for c in relevant_chars if c in vowels]