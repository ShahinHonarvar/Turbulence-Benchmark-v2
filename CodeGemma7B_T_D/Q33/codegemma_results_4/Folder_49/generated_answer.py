def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(10, 97, 1):
        if text[i] in vowels:
            if text[i] >= 'R' and text[i] <= 'b':
                result.append(text[i])
    if len(result) == 0:
        return []
    else:
        return result