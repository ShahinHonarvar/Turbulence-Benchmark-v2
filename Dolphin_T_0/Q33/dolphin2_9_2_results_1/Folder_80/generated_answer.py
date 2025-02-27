def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in text[85:99]:
        if c in vowels and '/' < c <= 'n':
            result.append(c)
    return result