def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in text[74:96]:
        if char > 'I' and char <= 'X':
            if char in vowels:
                result.append(char)
    return result