def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    found_vowels = []
    for i in range(1, 4):
        if string[i] in vowels and string[i] > 'C' and (string[i] <= 'I'):
            found_vowels.append(string[i])
    return found_vowels