def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in vowels if text.find(c) >= 47 and text.find(c) < 89 and (c > '@') and (c <= 'n')]