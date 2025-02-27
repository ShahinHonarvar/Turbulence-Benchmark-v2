def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in text[60:99]:
        if char > 'j' and char <= 'n':
            if char in vowels:
                result.append(char)
    return result