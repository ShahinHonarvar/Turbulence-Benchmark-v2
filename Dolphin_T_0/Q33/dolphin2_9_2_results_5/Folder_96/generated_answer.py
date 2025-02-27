def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for i in range(77, 84):
        if '(' < string[i] <= 'G' and string[i] in vowels:
            output.append(string[i])
    return output