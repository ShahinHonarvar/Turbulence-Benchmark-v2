def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in text[14:60]:
        if 'D' < char <= 'v' and char in vowels:
            result.append(char)
    return result