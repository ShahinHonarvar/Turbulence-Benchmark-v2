def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i in range(11, 53):
        if word[i] in vowels and word[i] > '+' and (word[i] <= 'W'):
            filtered_vowels.append(word[i])
    return filtered_vowels