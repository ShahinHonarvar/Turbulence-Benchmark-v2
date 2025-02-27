def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i in range(529, 828):
        if string[i] in vowels and string[i] > 'U' and (string[i] <= 'l'):
            filtered_vowels.append(string[i])
    return filtered_vowels if filtered_vowels else []