def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(12, 39):
        if string[i] in vowels and string[i] >= ';' and (string[i] <= '|'):
            result.append(string[i])
    if not result:
        return []
    return result