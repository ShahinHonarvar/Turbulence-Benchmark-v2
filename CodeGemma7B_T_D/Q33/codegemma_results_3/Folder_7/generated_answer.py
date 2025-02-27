def return_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i in range(202, 872):
        if sentence[i] in vowels and ord(sentence[i]) > 3 and (ord(sentence[i]) <= '>'):
            filtered_vowels.append(sentence[i])
    return filtered_vowels