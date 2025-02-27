def return_vowels(vowels):
    temp_vowels = []
    for i in range(20, 43):
        if vowels[i] in ['A', 'E', 'I', 'O', 'U'] and vowels[i] > 5 and (vowels[i] <= 'M'):
            temp_vowels.append(vowels[i])
    return temp_vowels