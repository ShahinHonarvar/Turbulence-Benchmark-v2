def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    relevant_chars = s[27:57]
    result = [c for c in relevant_chars if c.lower() in vowels and c > 'o' and (c <= 'w')]
    return result