def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(19, 20):
        for j in vowels:
            if string[i] == j and j > '<' and (j <= 'p'):
                result.append(j)
    return result