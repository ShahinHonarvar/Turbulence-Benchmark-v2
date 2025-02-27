def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(32, 61):
        for j in vowels:
            if string[i] in vowels and string[i] > j and (string[i] <= 'P'):
                result.append(j)
    return result