def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    result = []
    for i in range(23, 57):
        if text[i] in vowels and '0' < text[i] <= 'd':
            result.append(text[i])
    if not result:
        return []
    return result