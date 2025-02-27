def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(36, 56):
        if text[i] in vowels and text[i] > '+' and (text[i] <= '/'):
            result.append(text[i])
    return result