def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(21, 59):
        if index < len(text):
            char = text[index]
            if char in vowels and '/' < char <= 'a':
                result.append(char)
    return result