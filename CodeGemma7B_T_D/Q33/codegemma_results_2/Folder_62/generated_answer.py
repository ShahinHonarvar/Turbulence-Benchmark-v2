def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    found_vowels = []
    for i in range(14, 60):
        if word[i] in vowels and word[i] > 'D' and (word[i] <= 'v'):
            found_vowels.append(word[i])
    return found_vowels