def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(40, 91):
        if word[i] in vowels and word[i] > 'A' and (word[i] <= 'x'):
            result.append(word[i])
    return result