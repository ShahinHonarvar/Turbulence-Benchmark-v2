def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in text[12:39]:
        if char > ';' and char <= '|':
            if char.lower() in vowels:
                result.append(char)
    return result