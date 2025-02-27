def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in text[71:81]:
        if char in vowels:
            result.append(char)
    return result