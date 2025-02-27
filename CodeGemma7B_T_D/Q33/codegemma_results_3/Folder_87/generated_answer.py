def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = []
    for i in range(34, 58):
        if string[i] in vowels and 'b' < string[i] <= 'o':
            filtered_vowels.append(string[i])
    return filtered_vowels