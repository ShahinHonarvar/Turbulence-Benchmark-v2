def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i in range(43, 70):
        if string[i] in vowels and string[i] > '*' and (string[i] <= 'b'):
            filtered_vowels.append(string[i])
    return filtered_vowels or []