def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    if len(text) <= 323:
        return result
    for i in range(323, min(526, len(text))):
        if text[i] in vowels and '+' < text[i] <= ':':
            result.append(text[i])
    return result