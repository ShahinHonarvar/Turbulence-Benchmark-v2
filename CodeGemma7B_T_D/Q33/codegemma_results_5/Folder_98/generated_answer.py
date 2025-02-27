def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, char in enumerate(text[3:9]):
        if char in vowels and 'S' < char <= 'U':
            result.append(char)
    return result