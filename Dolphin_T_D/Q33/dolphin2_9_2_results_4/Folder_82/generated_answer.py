def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in text[86:99]:
        if char > 'E' and char <= 'r' and (char in vowels):
            result.append(char)
    return result