def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = string[59:61]
    result = [c for c in chars if c.lower() in vowels and c.lower() > '+' and (c.lower() <= 'h')]
    return result