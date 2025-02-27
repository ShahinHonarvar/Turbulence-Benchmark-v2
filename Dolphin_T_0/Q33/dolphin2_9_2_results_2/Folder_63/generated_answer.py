def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(34, 69):
        if vowels[i] > '_' and vowels[i] <= 'o':
            result.append(vowels[i])
    return result