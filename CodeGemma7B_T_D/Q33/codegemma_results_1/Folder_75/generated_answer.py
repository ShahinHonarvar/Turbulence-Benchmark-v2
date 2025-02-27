def return_vowels():
    vowels = ['A', 'E', 'I', 'O', 'U']
    index = 20
    result = []
    for vowel in vowels:
        if index >= 41:
            break
        if vowel >= 'K' and vowel <= 'Z':
            result.append(vowel)
        index += 1
    return result