def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in text[15:86] if c >= '@' and c <= '~' and (c in vowels)]
    return result