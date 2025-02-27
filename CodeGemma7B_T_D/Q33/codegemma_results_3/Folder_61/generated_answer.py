def return_vowels(code):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(1, 4):
        if code[i] in vowels and code[i] > 'C' and (code[i] <= 'I'):
            result.append(code[i])
    return result