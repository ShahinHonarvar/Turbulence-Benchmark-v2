def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for index in range(149, 313):
        if index < len(text):
            char = text[index]
            if char in vowels and 'M' < char <= 'j':
                result.append(char)
    return result